select distinct
  pl.url
from
  moz_bookmarks bk_child
  join moz_bookmarks bk_parent on bk_child.parent = bk_parent.id
  join moz_places pl on bk_child.fk = pl.id
where
  url like 'http%'
order by
  bk_child.dateAdded desc

