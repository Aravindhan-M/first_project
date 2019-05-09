import functools
def sort_plan(func):

    def sort_ordering(reverse,*args,**kwargs):
        model = kwargs['model']
        qs = kwargs['qs']
        pk_name = ('id' if not getattr(model._meta, 'pk', None)
                   else model._meta.pk.attname)
        pk_name = '%s.%s' % (model._meta.db_table, pk_name)
        pk_list = [q.id for q in sorted(qs, key=lambda qs: qs.mf_value,reverse=reverse)]
        clauses = ' '.join(['WHEN %s=%s THEN %s' % (pk_name,pk, i) for i, pk in enumerate(pk_list)])

        ordering = 'CASE %s END' % clauses
        return qs.filter(pk__in=pk_list).extra(
            select={'ordering': ordering}, order_by=('ordering',))

    @functools.wraps(func)
    def wrap(*args,**kwargs):
        sort = kwargs['sort']
        qs = kwargs['qs']
        if sort == "fee":
            return sort_ordering(False,*args,**kwargs)
        elif sort == "-fee":
            return sort_ordering(True,*args,**kwargs)
        else:
            return qs.order_by(sort)
    return wrap
