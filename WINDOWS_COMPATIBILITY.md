# Compatibilidad con Windows

## ✅ Problema Resuelto

Este proyecto ahora es **totalmente compatible con Windows** gracias al reemplazo de `simple_term_menu` por `questionary`.

## 🎉 Cambios Realizados

### Versión Anterior (Incompatible con Windows)
- ❌ Usaba `simple_term_menu` que depende de `termios` (solo Unix/Linux)
- ❌ No funcionaba en Windows nativamente

### Versión Actual (Compatible con Windows, Linux y Mac)
- ✅ Usa `questionary` que es multiplataforma
- ✅ Funciona en Windows, Linux y macOS
- ✅ Interfaz de menú moderna y colorida
- ✅ Soporte completo para todos los modos (menu, list, edit, delete, export, hack)

## 🚀 Instalación y Uso en Windows

### 1. Instalar Dependencias

```powershell
pip install -r requirements.txt
```

### 2. Ejecutar el Programa

#### Modo Menú Interactivo (Ahora funciona en Windows!)
```powershell
python main.py menu
```

#### Comandos CLI
```powershell
# Listar información
python main.py list

# Listar información específica
python main.py list -p -u  # passwords y URLs

# Editar usuario
python main.py edit bandit1 -p "nueva_password"

# Exportar datos
python main.py export -p reporte.pdf -f "user,password,details"

# Hackear un nivel
python main.py hack bandit1
```

## 📋 Características del Nuevo Menú

- **Navegación con flechas:** ↑ ↓ para moverse entre opciones
- **Selección:** Enter para seleccionar
- **Selección múltiple:** Espacio para marcar/desmarcar, Enter para confirmar
- **Salir:** Ctrl+C o Esc para salir del menú
- **Colores:** Interfaz colorida con tema verde (estilo hacker)

## 🔧 Solución de Problemas

### Si ves caracteres extraños en la consola
Ejecuta esto antes de usar el programa:
```powershell
chcp 65001
```

Esto configura la consola de Windows para usar UTF-8.

### Si los colores no se muestran correctamente
Usa Windows Terminal (recomendado) en lugar del CMD tradicional:
1. Instala Windows Terminal desde Microsoft Store
2. Ejecuta el programa desde Windows Terminal

## 📝 Notas Técnicas

### Módulos Reemplazados
- `simple_term_menu` → `questionary`
- Los emojis en mensajes fueron reemplazados por texto para mejor compatibilidad

### Dependencias Específicas de Plataforma
- `pexpect`: Solo se instala en sistemas Unix (Linux/Mac)
- No es necesario en Windows ya que se usan métodos alternativos

## 🎮 Prueba Rápida

Para verificar que todo funciona:

```powershell
# Mostrar ayuda general
python main.py --help

# Mostrar ayuda del modo list
python main.py list --help

# Probar el menú interactivo
python main.py menu
```

## 🌟 Recomendaciones para Windows

1. **Usa Windows Terminal** para mejor experiencia visual
2. **Configura UTF-8** con `chcp 65001`  
3. **Usa PowerShell 7+** para mejor compatibilidad
4. **Ten Python 3.10+** instalado

## 🐛 Reportar Problemas

Si encuentras algún problema en Windows, por favor reporta:
- Versión de Windows
- Versión de Python
- Terminal que estás usando (CMD, PowerShell, Windows Terminal)
- Mensaje de error completo

---

**¡Ahora puedes disfrutar del proyecto en Windows sin problemas!** 🎉
