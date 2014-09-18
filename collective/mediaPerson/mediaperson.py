from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from collective.mediaPerson import MessageFactory as _


# Interface class; used to define content-type schema.

class ImediaPerson(form.Schema, IImageScaleTraversable):
    """
    Folderish Person built with Dexterity
    """

    title = schema.TextLine(
        title=_(u"Name"),
    )

    bornDate = schema.Datetime(
        title=_(u"Born date"),
        required=False,
    )

    diedDate = schema.Datetime(
        title=_(u"Died date"),
        required=False,
    )

    body = RichText(
        title=_(u"Biography"),
        required=False,
    )

    @invariant
    def validateBornDateDiedDate(data):
        if data.bornDate is not None and data.diedDate is not None:
            if data.bornDate > data.diedDate:
                raise StartBeforeEnd(_(
                    u"The born date must be before the died date."))
    

    


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class mediaPerson(dexterity.Container):
    grok.implements(ImediaPerson)

    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# mediaperson_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class View(grok.View):
    grok.context(ImediaPerson)
    grok.require('zope2.View')

    # grok.name('view')