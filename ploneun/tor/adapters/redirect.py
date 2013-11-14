from inigo.redirecttocontainer.base import BaseRedirector
from five import grok
from Products.ATContentTypes.interfaces.file import IATFile
from plone.app.blob.interfaces import IATBlobFile
from ploneun.tor.content.tor_facility_form import ITORFacilityForm


class RedirectFileToMissionReport(BaseRedirector):
    grok.context(IATFile)
    grok.name('ploneun.tor.redirectfiletoTOR')
    container_iface = ITORFacilityForm
    direct_parent = True


class RedirectBlobFileToMissionReport(BaseRedirector):
    grok.context(IATBlobFile)
    grok.name('ploneun.tor.redirectblobfiletoTOR')
    container_iface = ITORFacilityForm
    direct_parent = True
