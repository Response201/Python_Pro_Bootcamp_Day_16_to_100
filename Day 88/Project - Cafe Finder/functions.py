from forms import CafesForm_search


def filter(request, Cafe):
    form = CafesForm_search(request)
    query = Cafe.query

    if form.name.data:
        query = query.filter(Cafe.name.ilike(f"%{form.name.data}%"))

    if form.location.data:
        query = query.filter(Cafe.location.ilike(f"%{form.location.data}%"))

    if form.has_wifi.data:
        query = query.filter(Cafe.has_wifi == True)

    if form.has_toilet.data:
        query = query.filter(Cafe.has_toilet == True)

    if form.has_sockets.data:
        query = query.filter(Cafe.has_sockets == True)

    if form.can_take_calls.data:
        query = query.filter(Cafe.can_take_calls == True)

    cafes = query.all()
    return cafes, form
