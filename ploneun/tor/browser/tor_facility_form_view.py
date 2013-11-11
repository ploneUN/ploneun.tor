from five import grok
from plone.directives import dexterity, form
from ploneun.tor.content.tor_facility_form import ITORFacilityForm

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(ITORFacilityForm)
    grok.require('zope2.View')
    grok.template('tor_facility_form_view')
    grok.name('view')

