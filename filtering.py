from model import session, Entry
from sqlalchemy import func, or_

objects = session.query(Entry).filter(or_(
    func.lower(Entry.title).like("%deep%"),
    func.lower(Entry.title).like("%learning%"),
    func.lower(Entry.title).like("%neural%"),
    func.lower(Entry.title).like("%network%"),
    func.lower(Entry.abstract).like("%deep%"),
    func.lower(Entry.abstract).like("%learning%"),
    func.lower(Entry.abstract).like("%neural%"),
    func.lower(Entry.abstract).like("%network%"))
).filter(Entry.abstract != None).all()

for o in objects:
    print \
        """
Title: \t\t %s
Abstract: \t %s
""" % (o.title, o.abstract)
