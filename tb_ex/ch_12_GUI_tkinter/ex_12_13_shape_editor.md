# Shape Editor

## Exercise

Build a small drawing editor inspired by `sc_12_09_canvas_demo.py`.
Organize the program as a class named `ShapeEditor`. The user should be
able to select a shape with the mouse and enter new dimensions for it.
Use `ex_12_13_shape_editor_start.py` as your starting point.

The starter provides the input-dialog code, including input limits and
cancellation checks, because dialogs have not been covered previously.
Read the explanation below to understand the supplied code. Your tasks
are to create the shapes, implement mouse selection, read the selected
shape's coordinates, and apply the new dimensions. In `resize_selected()`,
replace the marked placeholder `return` with the coordinate assignment
before trying the dialogs. Keep the other `return` statements.

The window should contain:

- A white Canvas, 500 pixels wide and 350 pixels high.
- At least two rectangles and two ovals with different fill colours.
  Place the shapes apart so each is easy to click. Give every shape
  a black outline and a positive width and height.
- A short instruction telling the user to click a shape to select it.
- A **Resize selected** button.

Implement the following behaviour:

1. Clicking a shape selects it. Mark the selection with a red outline
   of width 3. Restore the previous selection to a black outline of
   width 1. Preserve each shape's fill colour.
2. Clicking an empty part of the Canvas clears the selection.
3. Clicking **Resize selected** does nothing if no shape is selected.
   Otherwise, open one dialog for the new width and then one for the
   new height. Show the current dimensions as the initial values.
4. Keep the upper-left corner of the shape's bounding rectangle fixed.
   Restrict the new dimensions so that the entire bounding rectangle
   stays within the Canvas. Use a minimum dimension of 10 pixels.
5. Apply the new dimensions only after both dialogs have been accepted.
   If the user cancels either dialog, leave the shape unchanged.
   Keep the resized shape selected.

Use instance attributes for the Canvas and the selected shape's ID.
Use methods for creating the initial shapes, selecting a shape, and
resizing the selection. Use the rectangle and oval creation methods
from the Canvas demo; triangles are outside the scope of this exercise.

## Canvas techniques

### Shape IDs and mouse events

`create_rectangle(...)` and `create_oval(...)` return an integer ID
identifying the new Canvas item. Store the selected ID in
`self.selected_id`; use `None` when nothing is selected.

Connect the left mouse button to an instance method:

```python
self.canvas.bind("<Button-1>", self.select_shape)
```

The method must accept `event` in addition to `self`. For this Canvas,
which has no scrolling, `event.x` and `event.y` give the click position
in Canvas coordinates. A button's `command` callback, in contrast,
does not receive a mouse event.

### Finding the clicked shape

```python
items = self.canvas.find_overlapping(event.x, event.y,
                                     event.x, event.y)
```

With the same click coordinates repeated, `find_overlapping()` finds
shapes at the point clicked. The method name refers to items touching
the search area; you do not need to draw overlapping shapes.

The result is a tuple of shape IDs. An empty tuple means that the click
hit no shape. Otherwise, use `items[-1]` as the selected ID. If resizing
later makes shapes cover one another, this selects the visible shape
on top. All drawing items in this exercise should be filled rectangles
or ovals.

Do not use `find_closest()` here: it finds the nearest item even if
the user clicks an empty area.

### Marking the selection

Change an existing item's appearance with `itemconfig()`:

```python
self.canvas.itemconfig(item_id, outline="red", width=3)
```

Here, `width` is the outline thickness, not the shape's width. Restore
the previous selection before marking the new one. Check for `None`
before trying to configure a selected item.

### Reading and changing dimensions

For a rectangle or oval, `coords(item_id)` returns the four coordinates
of its bounding rectangle:

```python
x0, y0, x1, y1 = self.canvas.coords(item_id)
```

The width is `x1 - x0` and the height is `y1 - y0`. An oval fits inside
this rectangle. Canvas coordinates may be returned as floating-point
numbers; convert dimensions to `int` for the integer dialogs below.

Supplying new coordinates changes the existing item:

```python
self.canvas.coords(item_id, x0, y0, x0 + new_width, y0 + new_height)
```

This preserves the item's ID, colour, and selection outline. There is
no need to delete the shape and create it again.

## Introducing input dialogs

A dialog is a small window used to request input. Import Tkinter's
ready-made input dialogs with:

```python
from tkinter import simpledialog
```

Use `askinteger()` to request a whole number, for example:

```python
new_width = simpledialog.askinteger(
    "Resize shape", "New width in pixels:",
    parent=self.root,
    initialvalue=int(x1 - x0),
    minvalue=10,
    maxvalue=int(self.canvas_width - x0))
```

The first argument is the dialog title and the second is its prompt.
`parent` associates the dialog with the main window. `initialvalue`
prefills the input field. `minvalue` and `maxvalue` specify the inclusive
allowed range; the dialog asks the user to correct invalid input.

The call waits for the user to close the dialog while Tkinter continues
to handle the interface. It returns an integer when the user accepts,
or `None` if the user cancels or closes the dialog. Do not create
another `Tk()` object or call another `mainloop()` for these dialogs.

Check `if new_width is None:` and return without changing the shape
if the dialog was cancelled. Request the height in the same way, using
`self.canvas_height - y0` as its maximum. Check for cancellation again.
Only then call `coords()` to apply both new dimensions together.

## Suggested checks

- Select each kind of shape and verify that only one is marked.
- Click an empty area and then click **Resize selected**.
- Resize a rectangle and an oval; check that their upper-left corners
  stay fixed and their fill colours stay unchanged.
- Cancel the width dialog. Then accept a width but cancel the height
  dialog. Neither action should change the shape.
- Try text, dimensions below 10, and dimensions that would extend
  beyond the Canvas. The dialogs should reject these values.

## Assessment criteria

| Criterion | Description | Weight (%) |
|---|---|---:|
| Initial shapes | Create at least two rectangles and two ovals with different fill colours, black outlines, and separated positions inside the Canvas. | 20 |
| Mouse selection | Select the clicked shape, mark it with a red outline of width 3, restore the previous outline, and clear the selection when clicking empty space. | 35 |
| Resizing | Read the selected shape's dimensions and apply the accepted width and height while keeping its upper-left corner, fill colour, and selection unchanged. Preserve the supplied input limits and cancellation behaviour. | 35 |
| Class structure | Use ShapeEditor with instance attributes for the Canvas and selection, and methods for shape creation, selection, and resizing. | 10 |
| **Total** | | **100%** |
