# Fine Tuning LLMs
- Fine-tuning needs high GPU power, but PEFT (Parameter-Efficient Fine-Tuning) reduces costs by training fewer parameters. PEFT 2 techniques: LoRA and QLoRA.
- LoRA (Low-Rank Adaptation) adds small trainable layers while keeping most of the model frozen, making fine-tuning efficient.
- QLoRA (Quantized Low-Rank Adaptation) first quantizes the model (e.g., 4-bit) before applying LoRA, enabling fine-tuning on smaller GPUs.
- Quantization compresses model weights, reducing memory usage and speeding up inference with minimal accuracy loss.