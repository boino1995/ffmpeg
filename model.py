import subprocess
import tempfile

class Model:
    def __init__(self, **kwargs):
        pass

    def load(self):
        # Runs once when the container starts up
        pass

    def predict(self, model_input: dict):
        input_url = model_input.get("input_url")
        
        # Create a temporary file path for the output
        output_file = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False)
        output_path = output_file.name
        output_file.close()

        # Build your FFmpeg command
        cmd = [
            "ffmpeg",
            "-y",
            "-i", input_url,
            "-c:v", "libx264",
            "-preset", "veryfast",
            "-c:a", "aac",
            output_path
        ]

        try:
            process = subprocess.run(
                cmd, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                text=True, 
                check=True
            )
            
            return {
                "status": "success",
                "output_path": output_path
            }
            
        except subprocess.CalledProcessError as e:
            return {
                "status": "error",
                "stderr": e.stderr
            }