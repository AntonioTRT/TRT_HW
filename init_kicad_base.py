import os
import uuid
from datetime import datetime

# --- CONFIGURACIÓN ---
PROJECT_NAME = "carrier-board"
TARGET_DIR = os.path.join("hardware", "carrier-board")
TITLE = "STM32G474 Carrier Board - Base"

# Lista de componentes: (Ref, Value, Lib_ID, LCSC_Part, PosX, PosY)
COMPONENTS = [
    ("U1", "STM32G474RET6", "MCU_ST_STM32G4:STM32G474RETx", "C913074", 152.4, 101.6),
    ("J_USB", "USB-C", "Connector:USB_C_Receptacle_USB2.0_16pin", "C167339", 76.2, 76.2),
    ("U_LDO", "AP2112K-3.3", "Regulator_Linear:AP2112K-3.3TRG1", "C84949", 76.2, 127),
    ("J_SWD", "SWD Conn", "Connector_Generic:Conn_01x05", "C2897385", 228.6, 76.2),
    ("J_B2B", "Main Bus", "Connector_Generic:Conn_02x10_Odd_Even", "C2922180", 228.6, 127),
    ("U_ESD", "USBLC6-2SC6", "Protection:USBLC6-2SC6", "C87327", 101.6, 76.2)
]

# --- PLANTILLAS DE KICAD 8 (S-Expressions) ---

KICAD_PRO_TPL = """(kicad_project
  (version 1)
  (generator "gemini-cli-init-script")
  (main_schema "{project_name}.kicad_sch")
  (main_board "{project_name}.kicad_pcb")
)
"""

KICAD_SCH_HEADER_TPL = """(kicad_sch (version 20240108) (generator "gemini-cli-init-script")
  (uuid "{uuid}")
  (paper "A4")
  (title_block
    (title "{title}")
    (date "{date}")
    (rev "1.0")
  )
  (lib_symbols)
"""

SYMBOL_TPL = """  (symbol (lib_id "{lib_id}") (at {pos_x} {pos_y} 0) (unit 1)
    (in_bom yes) (on_board yes)
    (uuid "{uuid}")
    (property "Reference" "{ref}" (at {pos_x} {pos_y_ref} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "{value}" (at {pos_x} {pos_y_val} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Footprint" "" (at {pos_x} {pos_y} 0) (effects (font (size 1.27 1.27)) (hide yes)))
    (property "Datasheet" "" (at {pos_x} {pos_y} 0) (effects (font (size 1.27 1.27)) (hide yes)))
    (property "LCSC" "{lcsc}" (at {pos_x} {pos_y} 0)
      (effects (font (size 1.27 1.27)) (hide yes))
    )
  )"""

# --- FUNCIÓN PRINCIPAL ---

def main():
    """Generates the KiCad project structure and files."""
    
    # Asegurar que el directorio de hardware exista
    if not os.path.exists(TARGET_DIR):
        print(f"Creating directory: {TARGET_DIR}")
        os.makedirs(TARGET_DIR)

    # 1. Crear el archivo .kicad_pro
    pro_path = os.path.join(TARGET_DIR, f"{PROJECT_NAME}.kicad_pro")
    pro_content = KICAD_PRO_TPL.format(project_name=PROJECT_NAME)
    with open(pro_path, "w", encoding="utf-8") as f:
        f.write(pro_content)
    print(f"Created KiCad project file: {pro_path}")

    # 2. Crear el archivo .kicad_sch
    sch_path = os.path.join(TARGET_DIR, f"{PROJECT_NAME}.kicad_sch")
    
    # Cabecera del esquemático
    sch_content = KICAD_SCH_HEADER_TPL.format(
        uuid=uuid.uuid4(),
        title=TITLE,
        date=datetime.now().strftime("%Y-%m-%d")
    )
    
    # Añadir cada componente
    for ref, value, lib_id, lcsc, pos_x, pos_y in COMPONENTS:
        symbol_str = SYMBOL_TPL.format(
            lib_id=lib_id,
            pos_x=pos_x,
            pos_y=pos_y,
            uuid=uuid.uuid4(),
            ref=ref,
            value=value,
            lcsc=lcsc,
            pos_y_ref=pos_y - 5.08, # Un poco arriba
            pos_y_val=pos_y + 5.08  # Un poco abajo
        )
        sch_content += symbol_str

    # Cierre del archivo
    sch_content += "\n)"

    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(sch_content)
    print(f"Created KiCad schematic file: {sch_path}")
    print("\nProject initialization complete.")


if __name__ == "__main__":
    main()
