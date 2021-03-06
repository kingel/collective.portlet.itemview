from zope.i18nmessageid import MessageFactory
messageFactory = MessageFactory('collective.portlet.itemview')
_ = messageFactory

portlet_title          = _(u"portlet_title", default=u"Item portlet view")
portlet_description    = _(u"portlet_description", default=u"A portlet which can render an item.")
portlet_target_title   = _(u"Item")
portlet_target_desc    = _(u"portlet_target_desc", default=u"Find an item to display")
portlet_viewname_title = _(u"View")
portlet_viewname_desc  = _(u"portlet_viewname_desc", default=u"view used to render this item")
portlet_addform_title  = _(u"Add Item View portlet")
portlet_addform_desc   = _(u"portlet_addform_desc", default=u"This portlet displays an item with a selected view")
portlet_editform_title = _(u"Edit Item View Portlet")
portlet_editform_desc  = _(u"portlet_editform_desc", default=u"This portlet displays an item with a selected view.")
