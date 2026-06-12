---
title: "Media Library"
id: "ex_10_06_media_library"
tags: ["ABC", "abstractmethod", "inheritance", "composition", "isinstance", "polymorphism"]
difficulty: "medium"
prerequisites: ["ABC", "abstractmethod", "inheritance", "super()", "isinstance", "list"]
learning_outcomes:
  - "Design an ABC hierarchy with multiple concrete subclasses"
  - "Use composition: Library contains MediaItems"
  - "Filter a mixed collection using isinstance()"
  - "Implement __str__ consistently through a hierarchy"
---

# Media Library

## Exercise

Build a media library that can hold different types of media.

### MediaItem (ABC)

**Attributes:** `_title`, `_year`, `_rating` (1-5, default 0 = unrated)

**Abstract method:** `media_type()` - returns a string like "Movie", "Book"

**Methods:**
- `rate(score)` - set rating, validate 1-5
- `__str__()` - e.g. `[Movie] Inception (2010) ★★★★★`
- `__lt__()` - compare by rating

### Movie(MediaItem)

**Additional attributes:** `_director`, `_duration_min`

### Book(MediaItem)

**Additional attributes:** `_author`, `_pages`

### Podcast(MediaItem)

**Additional attributes:** `_host`, `_num_episodes`

### Library

**Composition:** holds a list of `MediaItem` objects.

**Methods:**
- `add(item)` - add any MediaItem
- `top_rated(n)` - return n highest rated items
- `by_type(media_type_str)` - return items matching the type string
- `search(query)` - case-insensitive partial match on title
- `__len__()` and `__str__()`

## Example run

```
Library: 5 items

Top 3:
  [Book]    The Pragmatic Programmer (1999) ★★★★★
  [Movie]   Inception (2010) ★★★★☆
  [Podcast] Lex Fridman Podcast (2018) ★★★★☆

Movies:
  [Movie] Inception (2010) ★★★★☆
  [Movie] The Matrix (1999) ★★★★★

Search 'prag':
  [Book] The Pragmatic Programmer (1999) ★★★★★
```

## Topics

- ABC with multiple concrete subclasses
- Composition: Library owns MediaItems
- `isinstance()` vs `media_type()` for filtering
- Sorting with `__lt__`

---
## Instructor notes

**Learning objectives covered:** ABC, multiple subclasses, composition,
polymorphism, filtering

**Two filtering approaches:** Students can filter by `isinstance(item, Movie)`
or by `item.media_type() == "Movie"`. Both work - worth discussing which is
more extensible. The `media_type()` approach does not require importing the
subclass, which is better for loose coupling.

**Star rating display:**
```python
stars = "★" * self._rating + "☆" * (5 - self._rating)
```
A small but satisfying detail that makes the output concrete.
