``mathtext`` now supports ``\text``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``\text`` can be used to obtain upright text within an equation.

.. code-block:: python

import matplotlib.pyplot as plt
plt.text(0.1, 0.5, r"$a = \sin(\phi) \text{ such that } \phi = \frac{x}{y}$")
plt.draw()
