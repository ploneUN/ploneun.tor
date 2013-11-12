from Acquisition import aq_inner
from zope.interface import Interface
from five import grok
from zope.component import getMultiAdapter
from Products.CMFCore.interfaces import IContentish
from plone.app.layout.viewlets import interfaces as manager
from ploneun.tor.interfaces import IProductSpecific
from ploneun.consultant.content.consultant import IConsultant
from ploneun.tor.backref import back_references
from ploneun.tor.content.tor_facility_form import ITORFacilityForm

grok.templatedir('templates')


class consultanttors(grok.Viewlet):
    grok.context(IConsultant)
    grok.viewletmanager(manager.IBelowContent)
    grok.template('consultant_tors')
    grok.layer(IProductSpecific)

    def available(self):
        return True

    def related_tors(self):
        return back_references(self.context, 'related_consultant')
