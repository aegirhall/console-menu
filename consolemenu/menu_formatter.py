from consolemenu.format.menu_style import MenuStyle
from consolemenu.format.menu_borders import MenuBorderStyle
from consolemenu.menu_component import Dimension, MenuHeader, MenuTextSection, MenuItemsSection, MenuFooter, MenuPrompt


class MenuFormatBuilder(object):

    def __init__(self, max_dimension=None):
        if max_dimension is None:
            max_dimension = Dimension(width=80, height=40)
        self.__max_dimension = max_dimension
        self.__header = MenuHeader(menu_style=MenuStyle(), max_dimension=max_dimension)
        self.__prologue = MenuTextSection(menu_style=MenuStyle(), max_dimension=max_dimension)
        self.__items_section = MenuItemsSection(menu_style=MenuStyle(), max_dimension=max_dimension)
        self.__epilogue = MenuTextSection(menu_style=MenuStyle(), max_dimension=max_dimension)
        self.__footer = MenuFooter(menu_style=MenuStyle(), max_dimension=max_dimension)
        self.__prompt = MenuPrompt(menu_style=MenuStyle(), max_dimension=max_dimension)
        # Indent items deeper than other sections
        self.__items_section.style.padding.left = 3
        # Change default top border of prompt to 0, so it hugs the bottom of the menu
        self.__prompt.style.padding.top = 0

    # ============================================================
    # Margins and Border style applies to entire menu
    # ============================================================

    def set_border_style(self, border_style):
        if not isinstance(border_style, MenuBorderStyle):
            raise TypeError('border_style must be type MenuBorderStyle')
        self.__header.style.border_style = border_style
        self.__prologue.style.border_style = border_style
        self.__items_section.style.border_style = border_style
        self.__epilogue.style.border_style = border_style
        self.__prompt.style.border_style = border_style
        return self

    def set_bottom_margin(self, bottom_margin):
        self.__footer.style.margins.bottom = bottom_margin
        return self

    def set_left_margin(self, left_margin):
        self.__header.style.margins.left = left_margin
        self.__prologue.style.margins.left = left_margin
        self.__items_section.style.margins.left = left_margin
        self.__epilogue.style.margins.left = left_margin
        self.__prompt.style.margins.left = left_margin
        return self

    def set_right_margin(self, right_margin):
        self.__header.style.margins.right = right_margin
        self.__prologue.style.margins.right = right_margin
        self.__items_section.style.margins.right = right_margin
        self.__epilogue.style.margins.right = right_margin
        self.__prompt.style.margins.right = right_margin
        return self

    def set_top_margin(self, top_margin):
        self.__header.style.margins.top = top_margin
        return self

    # ============================================================
    # Header Settings
    # ============================================================

    @property
    def title(self): return self.__header.title

    @property
    def subtitle(self): return self.__header.subtitle

    def set_title(self, title, align='left'):
        self.__header.title = title
        self.__header.title_align = align
        return self

    def set_subtitle(self, subtitle, align='left'):
        self.__header.subtitle = subtitle
        self.__header.subtitle_align = align
        return self

    def set_header_left_padding(self, x):
        self.__header.style.padding.left = x
        return self

    def set_header_right_padding(self, x):
        self.__header.style.padding.right = x
        return self

    def set_header_bottom_padding(self, x):
        self.__header.style.padding.bottom = x
        return self

    def set_header_top_padding(self, x):
        self.__header.style.padding.top = x
        return self

    # ============================================================
    # Footer Settings
    # ============================================================

    def set_footer_left_padding(self, x):
        self.__footer.style.padding.left = x
        return self

    def set_footer_right_padding(self, x):
        self.__footer.style.padding.right = x
        return self

    def set_footer_bottom_padding(self, x):
        self.__footer.style.padding.bottom = x
        return self

    def set_footer_top_padding(self, x):
        self.__footer.style.padding.top = x
        return self

    # ============================================================
    # Items Section Settings
    # ============================================================

    @property
    def items(self): return self.__items_section.items

    def add_item(self, item):
        self.__items_section.items.append(item)
        return self

    def set_items_left_padding(self, x):
        self.__items_section.style.padding.left = x
        return self

    def set_items_right_padding(self, x):
        self.__items_section.style.padding.right = x
        return self

    def set_items_bottom_padding(self, x):
        self.__items_section.style.padding.bottom = x
        return self

    def set_items_top_padding(self, x):
        self.__items_section.style.padding.top = x
        return self

    # ============================================================
    # Prologue Section Settings
    # ============================================================

    def set_prologue_text(self, text, align='left'):
        self.__prologue.text = text
        self.__prologue.text_align = align
        return self

    def show_prologue_top_border(self, flag):
        self.__prologue.show_top_border = flag
        return self

    def show_prologue_bottom_border(self, flag):
        self.__prologue.show_bottom_border = flag
        return self

    # ============================================================
    # Epilogue Section Settings
    # ============================================================

    def set_epilogue_text(self, text, align='left'):
        self.__epilogue.text = text
        self.__epilogue.text_align = align
        return self

    def show_epilogue_top_border(self, flag):
        self.__epilogue.show_top_border = flag
        return self

    def show_epilogue_bottom_border(self, flag):
        self.__epilogue.show_bottom_border = flag
        return self

    # ============================================================
    # Prompt Settings
    # ============================================================

    def set_prompt(self, prompt):
        self.__prompt.prompt = prompt
        return self

    # ============================================================
    # Menu generation
    # ============================================================

    def format(self):
        """
        Format the menu and return as a string.
        :return:  a string representation of the formatted menu.
        """
        content = ''
        sections = [self.__header]
        if self.__prologue.text is not None:
            sections.append(self.__prologue)
        sections.append(self.__items_section)
        if self.__epilogue.text is not None:
            sections.append(self.__epilogue)
        sections.append(self.__footer)
        sections.append(self.__prompt)
        for sect in sections:
            content += "\n".join(sect.generate())
            # Don't add newline to prompt so input is on same line as prompt
            if not isinstance(sect, MenuPrompt):
                content += "\n"
        return content