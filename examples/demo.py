from akuma import AkumaSubtitler, SubStyle

# Configuración
video_input = "input_video.mp4"
output_path = "output_video.mp4"
audio_track = "narration.mp3"
subs_file = None  # Generar automáticamente

# Estilo personalizado
inferno_style = SubStyle(
    font="Arial",
    size=24,
    color="#FF4500",
    border=3
)

# Procesar video
akuma = AkumaSubtitler()
akuma.forge_video(
    video_input=video_input,
    output_path=output_path,
    audio_track=audio_track,
    subs_file=subs_file,
    style=inferno_style
)

print("¡Video procesado con éxito! 🔥")