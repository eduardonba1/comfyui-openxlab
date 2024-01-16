import os
os.system(f"git lfs install")
os.system(f"git clone -b v1.4 https://github.com/camenduru/ComfyUI /home/xlab-app-center/ComfyUI")
os.chdir(f"/home/xlab-app-center/ComfyUI")
os.system(f"pip install -r requirements.txt")
os.system(f"git clone -b v1.4 https://github.com/camenduru/ComfyUI-Manager /home/xlab-app-center/ComfyUI/custom_nodes/ComfyUI-Manager")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.1/RealESRGAN_x2plus.pth -d /home/xlab-app-center/ComfyUI/models/upscale_models -o RealESRGAN_x2plus.pth")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/anything-v4.0/resolve/main/anything-v4.5-pruned.ckpt -d /home/xlab-app-center/ComfyUI/models/checkpoints -o anything-v4.5-pruned.ckpt")
os.system(f"python main.py --dont-print-server --port 7860 --enable-cors-header")
