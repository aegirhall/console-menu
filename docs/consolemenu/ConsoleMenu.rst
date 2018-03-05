ConsoleMenu --- Standard menu class
===================================

.. autoclass:: consolemenu.ConsoleMenu

    .. automethod:: consolemenu.ConsoleMenu.start
    .. automethod:: consolemenu.ConsoleMenu.join
    .. automethod:: consolemenu.ConsoleMenu.show

    .. raw:: html

        <h2>Item Management</h2>

    .. automethod:: consolemenu.ConsoleMenu.append_item
    .. automethod:: consolemenu.ConsoleMenu.add_exit
    .. automethod:: consolemenu.ConsoleMenu.remove_exit

    .. raw:: html

        <h2>User interaction</h2>

    .. automethod:: consolemenu.ConsoleMenu.get_input
    .. automethod:: consolemenu.ConsoleMenu.process_user_input
    .. automethod:: consolemenu.ConsoleMenu.draw
    .. automethod:: consolemenu.ConsoleMenu.go_to
    .. automethod:: consolemenu.ConsoleMenu.go_up
    .. automethod:: consolemenu.ConsoleMenu.go_down
    .. automethod:: consolemenu.ConsoleMenu.select
    .. automethod:: consolemenu.ConsoleMenu.exit

    .. raw:: html

        <h2>State management</h2>

    .. automethod:: consolemenu.ConsoleMenu.is_alive
    .. automethod:: consolemenu.ConsoleMenu.wait_for_start
    .. automethod:: consolemenu.ConsoleMenu.pause
    .. automethod:: consolemenu.ConsoleMenu.resume
    .. automethod:: consolemenu.ConsoleMenu.is_running
