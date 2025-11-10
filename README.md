## SOCF-SO-CLOUD

Aplicação mínima em **Flask** para evidenciar como uma app web observa **recursos de SO** (PID, memória, CPU e plataforma) e pode ser **implantada em PaaS (Render)** usando `gunicorn`.

---

### Objetivo do projeto
- Expor dois endpoints simples:
  - `GET /info` → retorna **JSON** com os **integrantes**.
  - `GET /metricas` → retorna **JSON** com:
    - `Nome` (integrantes)
    - `PID` (ID do processo da app)
    - `Memoria` (uso de RAM do processo, em MB)
    - `CPU` (uso de CPU do processo, em %)
    - `Sistema_Operacional` (p. ex., `Linux`, `Darwin`, `Windows`)
- Demonstrar que, mesmo em PaaS, a aplicação continua rodando sobre um **SO real** e consegue medir seus recursos de **processo**.

---

### Tecnologias
- **Python**
- **Flask**
- **psutil**
- **gunicorn**
- **Render**

---

### Endpoints (exemplos)

#### `/info`
```json
{
  "integrantes": "Guilherme Felippe Lazari e Danillo Gonçalves Camargo da Silva"
}
```
#### `/metricas`
```json
{
  "Nome": "Guilherme Felippe Lazari e Danillo Gonçalves Camargo da Silva",
  "PID": 58,
  "Memoria": "29.48 MB",
  "CPU": "0.0%",
  "Sistema_Operacional": "Linux"
}
```

### Desenvolvedores
**Guilherme Felippe Lazari**

**Danillo Gonçalves Camargo da Silva**

