import lib.constants as constants
import lib.utilities as utilities
import questionary
from questionary import Style

# Estilo personalizado para los menús
CUSTOM_STYLE = Style([
    ('qmark', 'fg:#00ff00 bold'),          # Token '?' marcador
    ('question', 'bold'),                   # Pregunta
    ('answer', 'fg:#00ff00 bold'),         # Respuesta seleccionada
    ('pointer', 'fg:#00ff00 bold'),        # Puntero '>'
    ('highlighted', 'fg:#00ff00 bold'),    # Opción resaltada
    ('selected', 'fg:#00ff00'),            # Opción seleccionada (checkbox)
    ('separator', 'fg:#cc5454'),           # Separadores
    ('instruction', ''),                   # Instrucciones
    ('text', ''),                          # Texto plano
])

def _create_menu_title(title):
    """Helper para crear títulos de menú consistentes."""
    return f"{title}\n{constants.KEYS_INSTRUCTIONS}"

# Configuraciones específicas de cada menú
MENU_CONFIGS = {
    "main": {
        "title": _create_menu_title("Main Menu"),
        "items": constants.MAIN_MENU
    },
    "list": {
        "title": _create_menu_title("LIST Info Menu"),
        "items": constants.LIST_MENU
    },
    "edit": {
        "title": _create_menu_title("EDIT Info Menu"),
        "items": constants.EDIT_MENU
    },
    "delete": {
        "title": _create_menu_title("DELETE Info Menu"),
        "items": constants.DELETE_MENU
    },
    "export": {
        "title": _create_menu_title("EXPORT Info Menu"),
        "items": utilities.get_export_menu_fields()
    },
    "select_user": {
        "title": f"Select User Menu\n{constants.KEYS_INSTRUCTIONS}",
        "items": constants.SELECT_USER_MENU
    }
}

class MenuWrapper:
    """Wrapper para mantener compatibilidad con el código existente."""
    def __init__(self, question_obj, is_multiselect=False, all_choices=None):
        self.question_obj = question_obj
        self.is_multiselect = is_multiselect
        self.chosen_menu_entries = []
        self.all_choices = all_choices or []
        
    def show(self):
        """Muestra el menú y retorna la selección."""
        try:
            result = self.question_obj.ask()
            
            if result is None:  # Usuario presionó Ctrl+C o Esc
                return None
                
            if self.is_multiselect:
                # Para checkbox, result es una lista de strings seleccionados
                self.chosen_menu_entries = result if result else []
                # Retornar lista de índices basada en las opciones seleccionadas
                if not result:
                    return None
                indices = [i for i, choice in enumerate(self.all_choices) if choice in result]
                return indices if indices else None
            else:
                # Para select, result es el string seleccionado
                # Retorna el índice de la opción seleccionada
                for i, choice in enumerate(self.all_choices):
                    if choice == result:
                        return i
                return None
        except (KeyboardInterrupt, EOFError):
            return None

def _create_questionary_menu(menu_type, is_multiselect=False, **kwargs):
    """
    Helper genérico para crear menús con questionary.
    """
    config = MENU_CONFIGS[menu_type]
    title = kwargs.get("title", config["title"])
    items = kwargs.get("menu_entries", config["items"])
    
    # Filtrar items vacíos si skip_empty_entries está activado
    if kwargs.get("skip_empty_entries", False):
        items = [item for item in items if item.strip()]
    
    if is_multiselect:
        question = questionary.checkbox(
            title,
            choices=items,
            style=CUSTOM_STYLE
        )
    else:
        question = questionary.select(
            title,
            choices=items,
            style=CUSTOM_STYLE
        )
    
    return MenuWrapper(question, is_multiselect, items), False

# Method that handles MAIN menu
def main_menu_config():
    return _create_questionary_menu(
        "main",
        title=constants.BANNER + "\n" + MENU_CONFIGS["main"]["title"]
    )

# Method that handles LIST menu
def list_menu_config():
    return _create_questionary_menu("list", is_multiselect=True)

# Method that handles EDIT menu
def edit_menu_config():
    return _create_questionary_menu("edit")

# Method that handles DELETE menu
def delete_menu_config():
    return _create_questionary_menu("delete")

# Method that handles EXPORT menu
def export_menu_config():
    return _create_questionary_menu(
        "export",
        menu_entries=utilities.get_export_menu_fields(),
        is_multiselect=True,
        skip_empty_entries=True
    )

# Method that handles SELECT USER menu
def select_user_menu_config(next_text, next_title):
    config = MENU_CONFIGS["select_user"]
    menu_entries = [next_text if x == "<default_text>" else x for x in config["items"]]
    return _create_questionary_menu(
        "select_user",
        menu_entries=menu_entries,
        title=f"{next_title} > {config['title']}"
    )
