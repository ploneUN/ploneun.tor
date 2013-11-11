from collective.grok import gs
from ploneun.tor import MessageFactory as _

@gs.importstep(
    name=u'ploneun.tor', 
    title=_('ploneun.tor import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('ploneun.tor.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
