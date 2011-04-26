from pyramid.response import Response
from .models import Entry
import deform
import couchdbkit

def list_entries(request):
    pass
    
def view_entry(request):
    pass

def insert_entry(request):
    entry_schema = Entry.get_schema()
    entry_form = deform.Form(entry_schema, buttons=('submit',))
    
    if 'submit' in request.POST:
        
        controls = request.POST.items()
        try:
            appstruct = entry_form.validate(controls)
        except deform.ValidationFailure, e:
            return Response(e.render())
  
        appstruct['type'] = 'Entry' #FIXME        

        entry = Entry.from_python(appstruct)
        entry._id = '10'
        entry_id = entry.save(request.db)
        
        return Response('Inserido com sucesso sob o ID ' + str(entry_id))

    return Response(entry_form.render())

def edit_entry(request):
    entry_schema = Entry.get_schema()
    entry_form = deform.Form(entry_schema, buttons=('submit',))
    
    if 'submit' in request.POST:
        #TODO
        controls = request.POST.items()
        try:
            appstruct = entry_form.validate(controls)
        except deform.ValidationFailure, e:
            return Response(e.render())
        appstruct['type'] = 'Entry' #FIXME
        appstruct['_rev'] = appstruct['_rev']+'1'
        entry = Entry.from_python(appstruct)
        entry_id = entry.save(request.db)
        
        return Response('Inserido com sucesso sob o ID ' + str(entry_id))

    else:
        
        try:
           entry = request.db.get(request.matchdict['id'])
        except couchdbkit.ResourceNotFound:
            raise exceptions.NotFound()
         
    return Response(entry_form.render(entry))
    

