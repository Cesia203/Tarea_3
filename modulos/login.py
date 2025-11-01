import streamlit as st
from modulos.config.conexion import obtener_conexion


def verificar_usuario(usuario, contrasena):
    con = obtener_conexion()
    if not con:
        st.error("âš ï¸ No se pudo conectar a la base de datos.")
        return None
    else:
        # âœ… Guardar en el estado que la conexiÃ³n fue exitosa
        st.session_state["conexion_exitosa"] = True

    try:
        cursor = con.cursor()
        query = "SELECT Tipo_usuario FROM USUARIO WHERE usuario = %s AND contrasena = %s"
        cursor.execute(query, (usuario, contrasena))
        result = cursor.fetchone()
        return result[0] if result else None
    finally:
        con.close()


def login():
    st.title("Inicio de sesiÃ³n")

    # ðŸŸ¢ Mostrar mensaje persistente si ya hubo conexiÃ³n exitosa
    if st.session_state.get("conexion_exitosa"):
        st.success("âœ… ConexiÃ³n a la base de datos establecida correctamente.")

    usuario = st.text_input("Usuario", key="usuario_input")
    contrasena = st.text_input("ContraseÃ±a", type="password", key="contrasena_input")

    if st.button("Iniciar sesiÃ³n"):
        tipo = verificar_usuario(usuario, contrasena)
        if tipo:
            st.session_state["usuario"] = usuario
            st.session_state["tipo_usuario"] = tipo
            st.success(f"Bienvenido ({tipo}) ðŸ‘‹")
            st.session_state["sesion_iniciada"] = True
            st.rerun()
        else:
            st.error("âŒ Credenciales incorrectas.")
