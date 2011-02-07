from plone.portlets.interfaces import IPortletDataProvider
from zope import component
from zope import schema
from zope import interface
from zope.formlib import form
from plone.app.portlets.portlets import base
from plone.memoize.compress import xhtml_compress
from plone.memoize.instance import memoize
from plone.app.vocabularies.catalog import SearchableTextSourceBinder
from plone.app.form.widgets.uberselectionwidget import UberSelectionWidget
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from collective.portlet.itemview import i18n

import logging
logger = logging.getLogger('collective.portlet.itemview')

class IItemViewPortlet(IPortletDataProvider):

    target = schema.Choice(
        title=u"Target Item",
        description=u"Find the collection which provides the items to list",
        required=True,
        source=SearchableTextSourceBinder(
            {},
            default_query='path:'))

class Assignment(base.Assignment):
    interface.implements(IItemViewPortlet)

    title = i18n.portlet_title
    target = None

    def __init__(self, target=None):
        self.target = target

class Renderer(base.Renderer):

    def render(self):
        templateview = "itemview_portlet"

        target = self.target()
        if target is None:
            return ""

        try:
            view = component.getMultiAdapter((target, self.request),
                                        name=templateview)
            return view()
        except component.ComponentLookupError, e:
            try:
                return target.restrictedTraverse(templateview)()
            except AttributeError:
                logger.error('no %s for %s'%(templateview, target.portal_type))
        return ""

    @memoize
    def target(self):
        """ get the collection the portlet is pointing to"""

        target_path = self.data.target
        if not target_path:
            return None

        if target_path.startswith('/'):
            target_path = target_path[1:]

        if not target_path:
            return None

        portal_state = component.getMultiAdapter((self.context, self.request),
                                       name=u'plone_portal_state')
        portal = portal_state.portal()
        if isinstance(target_path, unicode):
            #restrictedTraverse accept only strings
            target_path = str(target_path)
        return portal.restrictedTraverse(target_path, default=None)


class AddForm(base.AddForm):
    form_fields = form.Fields(IItemViewPortlet)
    form_fields['target'].custom_widget = UberSelectionWidget
    label = u"Add Item View portlet"
    description = u"This portlet displays an item with a selected view"

    def create(self, data):
        return Assignment()

class EditForm(base.EditForm):
    form_fields = form.Fields(IItemViewPortlet)
    form_fields['target'].custom_widget = UberSelectionWidget
    label = u"Edit Item View Portlet"
    description = u"This portlet displays an item with a selected view."