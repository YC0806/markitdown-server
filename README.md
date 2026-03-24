# MarkItDown Service

FastAPI 服务，封装 MarkItDown Python 库，提供 HTTP 接口进行文件格式转换为 Markdown。

## 项目结构

```
markitdown-server/
├── app/
│   └── main.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## 功能特性

- ✅ 支持多种文件格式转换为 Markdown（PDF、DOCX、PPTX、XLSX 等）
- ✅ 基于 FastAPI 的 RESTful API
- ✅ Docker 容器化部署
- ✅ 健康检查接口
- ✅ 临时文件自动清理

## 快速开始

### 本地开发

1. 安装依赖（需要 Python 3.10+）：

```bash
pip install -r requirements.txt
```

2. 启动服务：

```bash
fastapi dev app/main.py
```

3. 访问 API 文档：http://127.0.0.1:8000/docs

### Docker 部署

1. 构建镜像：

```bash
docker build -t markitdown-service:latest .
```

2. 启动容器：

```bash
docker run --rm -p 8000:8000 markitdown-service:latest
```

3. 健康检查：

```bash
curl http://127.0.0.1:8000/health
```

## API 接口

### GET /health

健康检查接口。

**响应示例：**
```json
{
  "status": "ok"
}
```

### POST /convert

文件转换接口，上传文件并转换为 Markdown。

**请求参数：**
- `file`: 上传的文件（multipart/form-data）

**响应示例：**
```json
{
  "filename": "test.pdf",
  "markdown": "# 文档标题\n\n文档内容..."
}
```

## 使用示例

### curl 调用

```bash
curl -X POST "http://127.0.0.1:8000/convert" \
  -F "file=@./test.pdf"
```

### Python 调用

```python
import requests

with open("test.pdf", "rb") as f:
    resp = requests.post(
        "http://127.0.0.1:8000/convert",
        files={"file": ("test.pdf", f, "application/pdf")},
        timeout=120,
    )

resp.raise_for_status()
data = resp.json()
print(data["markdown"])
```

### JavaScript/TypeScript 调用

```javascript
const formData = new FormData();
formData.append('file', fileInput.files[0]);

const response = await fetch('http://127.0.0.1:8000/convert', {
  method: 'POST',
  body: formData
});

const data = await response.json();
console.log(data.markdown);
```

## 支持的文件格式

- PDF (`.pdf`)
- Word 文档 (`.docx`, `.doc`)
- PowerPoint (`.pptx`, `.ppt`)
- Excel (`.xlsx`, `.xls`)
- 图片文件 (`.jpg`, `.png`, `.gif` 等)
- HTML (`.html`, `.htm`)
- 文本文件 (`.txt`, `.csv` 等)
- 更多格式请参考 [MarkItDown 官方文档](https://github.com/microsoft/markitdown)

## 依赖说明

- **FastAPI**: 现代高性能 Web 框架
- **MarkItDown**: Microsoft 开源的文件转换库
- **python-multipart**: 处理文件上传

## 后续增强方向

- [ ] 文件大小限制
- [ ] MIME 类型白名单
- [ ] API Key 鉴权
- [ ] `/convert-url` 接口（支持 URL 下载转换）
- [ ] OCR 插件支持
- [ ] 对象存储集成

## 许可证

MIT