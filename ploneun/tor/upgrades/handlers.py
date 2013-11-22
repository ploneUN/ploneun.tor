from collective.grok import gs
from Products.CMFCore.utils import getToolByName

# -*- extra stuff goes here -*- 


@gs.upgradestep(title=u'Upgrade ploneun.tor to 2',
                description=u'Upgrade ploneun.tor to 2',
                source='1', destination='2',
                sortkey=1, profile='ploneun.tor:default')
def to2(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-ploneun.tor.upgrades:to2')
