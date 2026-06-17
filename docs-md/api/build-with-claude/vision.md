# Vision

Copy page



This guide describes how to work with images in Claude, including best practices, code examples, and limitations to keep in mind.

---

##  How to use vision

Use Claude's vision capabilities through:

- [claude.ai](https://claude.ai/). Upload an image like you would a file, or drag and drop an image directly into the chat window.
- The [Console Workbench](/workbench). A button to add images appears at the top right of every User message block.
- API request. See the examples in this guide.

Multiple images can be included in a single request, which Claude will analyze jointly when formulating its response. This can be helpful for comparing or contrasting images.

---

##  Before you upload

###  General limits

The maximal number of images per message or request is:

- 20 per message on [claude.ai](https://claude.ai/).
- 100 per request on the API, for models with a 200k-token context window.
- 600 per request on the API, for all other models.

The maximal dimensions per image are 8000x8000 px.

If a single API request contains more than 20 images, a stricter per-image dimension limit applies. On Amazon Bedrock and Vertex AI, document blocks such as PDFs also count toward this threshold. Images exceeding the stricter limit are rejected with an `invalid_request_error` whose message references "many-image requests" and states the current limit in pixels. To stay under the limit on all platforms, either resize each image so that neither dimension exceeds 2000 px, or keep the request to 20 or fewer image and document blocks.

The maximal size per image is:

- 10 MB (base64-encoded) when using the Claude API directly.
- 5 MB (base64-encoded) on Amazon Bedrock and Vertex AI.
- 10 MB on [claude.ai](https://claude.ai/).



While the API supports up to 600 images per request, [request size limits](api/overview.md) (32 MB for standard endpoints; lower on some partner-operated platforms, for example, Amazon Bedrock and Vertex AI) can be reached first. For many images, consider uploading with the [Files API](#files-api-image-example) and referencing by `file_id` to keep request payloads small.

Even when using the Files API, requests with many large images can fail before reaching the 600-image count. Reduce image dimensions or file sizes (for example, by downsampling) before uploading (see [Evaluate image size](#evaluate-image-size)).

###  Evaluate image size

Claude views images in patches instead of pixels. Each patch is a 28×28 pixel block of the image, referred to as a visual token. An image therefore costs `⌈width / 28⌉ × ⌈height / 28⌉` visual tokens.

If Claude receives an image that is too large, it resizes it. The maximal native image resolution is:

- For Claude Fable 5 and Claude Mythos 5: 4784 tokens, and at most 2576 pixels on the long edge.
- For Claude Opus 4.8: 4784 tokens, and at most 2576 pixels on the long edge.
- For Claude Opus 4.7: 4784 tokens, and at most 2576 pixels on the long edge.
- For other models: 1568 tokens, and at most 1568 pixels on the long edge.



If your input image is larger than this native resolution, it is first resized to the largest possible size that preserves the aspect ratio. All images, resized or not, are then padded on the bottom and right edges to a multiple of 28 pixels. See [How Claude resizes and pads images](#how-claude-resizes-and-pads-images) for the exact rule.

When asking Claude to output coordinates (points, bounding boxes, and so on), it works best with absolute pixel coordinates expressed with respect to the resized image it sees. See [Working with coordinates and bounding boxes](#working-with-coordinates-and-bounding-boxes) for how to handle this.

To minimize latency and to simplify coordinate-based workflows, you should prefer resizing images before uploading them.

###  Calculate image costs

Each image you include in a request to Claude counts toward your token usage. To calculate the approximate cost, multiply the image's visual token count (see [Evaluate image size](#evaluate-image-size)) by the [per-token price of the model](https://claude.com/pricing) you're using.

Here are examples of tokenization and approximate costs for different image sizes within the API's size constraints based on Claude Sonnet 4.6 per-token price of $3 per million input tokens:

| Image size | # of Tokens | Cost / image | Cost / 1k images |
| --- | --- | --- | --- |
| 200x200 px(0.04 megapixels) | 64 | ~$0.00019 | ~$0.19 |
| 1000x1000 px(1 megapixel) | 1296 | ~$0.0039 | ~$3.89 |
| 1092x1092 px(1.19 megapixels) | 1521 | ~$0.0046 | ~$4.56 |
| 1920x1080 px(2.07 megapixels) | 1560 | ~$0.0047 | ~$4.68 |
| 2000x1500 px(3 megapixels) | 1564 | ~$0.0047 | ~$4.69 |
| 3840x2160 px(8.29 megapixels) | 1560 | ~$0.0047 | ~$4.68 |

Note that the last three images exceed the native resolution and are downscaled before processing (to 1456x819 px, 1270x952 px, and 1456x819 px respectively), which caps their token cost. The 4K image costs no more than the 1920x1080 image because both downscale to the same size; the extra resolution is discarded.

####  High-resolution image support

Claude Opus 4.7 is the first Claude model with high-resolution image support; Claude Opus 4.8, Claude Fable 5, Claude Mythos 5, and later models also support it. The maximum image resolution is 2576 pixels on the long edge, up from 1568 px on prior models. This unlocks performance gains on vision-heavy workloads and is particularly valuable for computer use, screenshot understanding, and document analysis.

High-resolution support is automatic on Claude Opus 4.7 and later models and requires no beta header or client-side opt-in.

High-resolution images on Claude Opus 4.7, Claude Opus 4.8, Claude Fable 5, and Claude Mythos 5 can use up to approximately 3x more image tokens than on prior models (4784 versus 1568 tokens per image). If you don't need the additional fidelity, downsample images before sending to control token costs.

Here are the same image sizes tokenized for Claude Opus 4.7 and Claude Opus 4.8, based on their per-token price of $5 per million input tokens:

| Image size | # of Tokens | Cost / image | Cost / 1k images |
| --- | --- | --- | --- |
| 200x200 px(0.04 megapixels) | 64 | ~$0.00032 | ~$0.32 |
| 1000x1000 px(1 megapixel) | 1296 | ~$0.0065 | ~$6.48 |
| 1092x1092 px(1.19 megapixels) | 1521 | ~$0.0076 | ~$7.61 |
| 1920x1080 px(2.07 megapixels) | 2691 | ~$0.013 | ~$13.46 |
| 2000x1500 px(3 megapixels) | 3888 | ~$0.019 | ~$19.44 |
| 3840x2160 px(8.29 megapixels) | 4784 | ~$0.024 | ~$23.92 |

Only the last image exceeds the higher limits: the 4K image is downscaled to 2576x1449 px before processing. High-resolution support raises the resolution limits but does not remove them; images larger than 2576 px on the long edge (or 4784 visual tokens) are still downscaled.

###  Ensure image quality

When providing images to Claude, keep the following in mind for best results:

- **Image format**: Use a supported image format: JPEG, PNG, GIF, or WebP.  
  Animations are unsupported, and only the first frame will be used.
- **Image clarity**: Ensure images are clear and not too blurry or pixelated.
- **Text**: If the image contains important text, make sure it's legible and not too small. Avoid cropping out key visual context just to enlarge the text.
- **Resizing**: Take into account that your image might be resized if it is too large (see above); this might for example make text less legible. Consider pre-resizing your images, cropping them, or both.
- **Image compression**: Compressing images before sending them, using a lossy format such as JPEG or WebP (lossy mode), can reduce latency by reducing the size of requests. However, this can introduce artifacts that are detrimental to model performance, especially when multiple compression passes are applied. For example, heavy JPEG compression can make text difficult to read. Confirm your compression settings are appropriate for the task by inspecting the actual images sent to the API.

---

##  Working with coordinates and bounding boxes

Claude can locate and label regions of an image (for example, returning bounding boxes for tables, form fields, chart elements, or UI components).



**Claude works best with absolute pixel coordinates.** Ask for them explicitly in your prompt. For example: *"Return the bounding box of each table as `[x1, y1, x2, y2]` in pixel coordinates."* Claude does not work well when you ask for normalized coordinates, for example: *"Return bounding box coordinates between `0` and `1000`."* Always ask for pixel coordinates and normalize in your own code if you need to.

Coordinates follow the standard image convention: the origin `(0, 0)` is the top-left corner of the image, with x increasing to the right and y increasing downward. The coordinates Claude returns are pixel positions in the image Claude sees: your image after Claude resizes it to fit the model's native resolution (see [How Claude resizes and pads images](#how-claude-resizes-and-pads-images)). To get coordinates you can use directly, either pre-resize your image so the coordinates map one-to-one onto the image you have (see [Resize your image before uploading](#resize-your-image-before-uploading)), or rescale the coordinates Claude returns (see [Rescale coordinates when you cannot pre-resize](#rescale-coordinates-when-you-cannot-pre-resize)).



Claude's spatial reasoning has limits (see [Limitations](#limitations)). Coordinate accuracy is best when you state the expected coordinate format in your prompt and spot-check results visually before processing at scale. For [PDF uploads](build-with-claude/pdf-support.md), pages are rasterized to images server-side at dimensions you don't control, so the returned coordinates can't be reliably mapped back onto the page. To work with coordinates on PDF content, rasterize the pages to images yourself and use the pre-resize approach.

###  How Claude resizes and pads images

Claude finds the largest aspect-preserving size that satisfies both of the model's image limits:

1. **Edge limit:** neither side exceeds the maximum edge length (1568 px for most models, 2576 px for Claude Opus 4.7 and later models).
2. **Visual token limit:** the image's token cost `⌈width / 28⌉ × ⌈height / 28⌉` does not exceed the model's visual token budget (1568 tokens for most models, 4784 for Claude Opus 4.7 and later models).

For most photos and screenshots the edge limit is what triggers a resize. For portrait documents the visual token limit usually triggers first, and overlooking it is the most common cause of misaligned coordinates. For example, an A4 page scanned at 130 DPI is 1075×1520 pixels: both sides are under 1568 px, but it costs `39 × 55 = 2145` visual tokens, so Claude resizes it to 924×1307.

Claude then pads every image, whether or not it was resized, up to the next multiple of 28 pixels on the bottom and right edges (924×1307 becomes 924×1316 in the example). The padding contains no content: Claude perceives the padded image, but the page content only ever occupies the un-padded resized region. **Always normalize or rescale by the resized dimensions, not the padded dimensions**; dividing by the padded dimensions scales every coordinate by a small amount.

###  Resize your image before uploading

The most reliable approach is to resize your image yourself before uploading, so the image you have is exactly the image Claude sees and the coordinates Claude returns need no conversion.

The following reference implementation computes the exact size Claude resizes an image to:

```shiki
import math

def count_image_tokens(width: int, height: int) -> int:
    """Visual tokens consumed by an image: one token per 28x28 pixel patch."""
    return math.ceil(width / 28) * math.ceil(height / 28)

def resized_size(
    width: int,
    height: int,
    max_edge: int = 1568,
    max_tokens: int = 1568,
) -> tuple[int, int]:
    """The size Claude resizes an image to before padding.

    Defaults are for most models. For Claude Opus 4.7 and later models, use
    max_edge=2576 and max_tokens=4784. Returns (width, height). Images that
    already fit within the limits are returned unchanged.
    """

    def fits(w: int, h: int) -> bool:
        return (
            math.ceil(w / 28) * 28 <= max_edge
            and math.ceil(h / 28) * 28 <= max_edge
            and count_image_tokens(w, h) <= max_tokens
        )

    if fits(width, height):
        return (width, height)
    if height > width:
        resized_h, resized_w = resized_size(height, width, max_edge, max_tokens)
        return (resized_w, resized_h)

    # Binary search along the long edge for the largest aspect-preserving
    # size that fits.
    aspect_ratio = width / height
    lo, hi = 1, width  # lo always fits; hi never fits
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if fits(mid, max(round(mid / aspect_ratio), 1)):
            lo = mid
        else:
            hi = mid
    return (lo, max(round(lo / aspect_ratio), 1))

# The A4 example from "How Claude resizes and pads images":
print(resized_size(1075, 1520))  # (924, 1307)
```



1. Resize the image to the dimensions returned by `resized_size`. If the image already fits within the model's limits, `resized_size` returns its dimensions unchanged and no resize is needed.
2. Send the resized image to the API. Don't pad it yourself; Claude handles padding, and padding doesn't shift the coordinate origin.
3. In your prompt, ask explicitly for pixel coordinates. For example: *"Return the bounding box of each table as `[x1, y1, x2, y2]` in pixel coordinates."*
4. Use the returned coordinates directly against the image you sent. If you need normalized coordinates, divide by the dimensions of the image you sent, not by the original image's dimensions and not by the padded dimensions.

###  Rescale coordinates when you cannot pre-resize

If you cannot pre-resize (for example, when the image comes from an upstream system you can't modify), use `resized_size` from [Resize your image before uploading](#resize-your-image-before-uploading) to recover the dimensions Claude saw, then map the coordinates Claude returns into normalized coordinates or back onto your original image. This approach requires knowing the pixel dimensions of the image you uploaded, so it does not apply to PDF uploads.

```shiki
def to_relative_coordinates(
    x: float,
    y: float,
    original_width: int,
    original_height: int,
    max_edge: int = 1568,
    max_tokens: int = 1568,
) -> tuple[float, float]:
    """Map a pixel coordinate returned by Claude to relative coordinates in [0, 1].

    Pass the dimensions of the image you uploaded. For Claude Opus 4.7 and
    later models, use max_edge=2576 and max_tokens=4784.
    """
    resized_w, resized_h = resized_size(
        original_width, original_height, max_edge, max_tokens
    )
    return (x / resized_w, y / resized_h)

# To express the coordinate in your original image's pixel space, multiply the
# relative coordinate by your original dimensions:
# (rel_x * original_width, rel_y * original_height)
```



Padding is applied only to the bottom and right edges, so the origin doesn't shift and a per-axis linear rescale is sufficient.

---

##  Prompt examples

Many of the [prompting techniques](build-with-claude/prompt-engineering/overview.md) that work well for text-based interactions with Claude can also be applied to image-based prompts.

These examples demonstrate best practice prompt structures involving images.



Just as [placing long documents before your query](build-with-claude/prompt-engineering/claude-prompting-best-practices.md) improves results in text prompts, Claude works best when images come before text. Images placed after text or interpolated with text still perform well, but if your use case allows it, prefer an image-then-text structure.

###  About the prompt examples

The following examples demonstrate how to use Claude's vision capabilities using various programming languages and approaches. You can provide images to Claude in three ways:

1. As a base64-encoded image in `image` content blocks
2. As a URL reference to an image hosted online
3. Using the Files API (upload once, use multiple times)



On Amazon Bedrock and Vertex AI, only base64-encoded sources are currently available.

The base64 example prompts use these variables:

cURLPythonTypeScriptC#GoJavaPHPRuby



```shiki
import base64
import httpx

# For base64-encoded images
image1_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
image1_media_type = "image/jpeg"
image1_data = base64.standard_b64encode(httpx.get(image1_url).content).decode("utf-8")

image2_url = "https://upload.wikimedia.org/wikipedia/commons/b/b5/Iridescent.green.sweat.bee1.jpg"
image2_media_type = "image/jpeg"
image2_data = base64.standard_b64encode(httpx.get(image2_url).content).decode("utf-8")

# For URL-based images, you can use the URLs directly in your requests
```

Below are examples of how to include images in a Messages API request using base64-encoded images and URL references:

###  Base64-encoded image example

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
image1_data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGP4z8AAAAMBAQDJ/pLvAAAAAElFTkSuQmCC"
image1_media_type = "image/png"

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image1_media_type,
                        "data": image1_data,
                    },
                },
                {"type": "text", "text": "Describe this image."},
            ],
        }
    ],
)
print(message)
```

###  URL-based image example

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "url",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
                    },
                },
                {"type": "text", "text": "Describe this image."},
            ],
        }
    ],
)
print(message)
```

###  Files API image example

For images you'll use repeatedly or when you want to avoid encoding overhead, use the [Files API](build-with-claude/files.md). Upload the image once, then reference the returned `file_id` in subsequent messages instead of resending base64 data.



In multi-turn conversations and agentic workflows, each request resends the
full conversation history. If images are base64-encoded, the full image bytes
are included in the payload on every turn, which can significantly increase
request size and latency as the conversation grows. Uploading images to the
Files API and referencing them by `file_id` keeps request payloads small
regardless of how many images accumulate in the conversation history.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

# Upload the image file
with open("image.jpg", "rb") as f:
    file_upload = client.beta.files.upload(file=("image.jpg", f, "image/jpeg"))

# Use the uploaded file in a message
message = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    betas=["files-api-2025-04-14"],
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {"type": "file", "file_id": file_upload.id},
                },
                {"type": "text", "text": "Describe this image."},
            ],
        }
    ],
)

print(message.content)
```

See [Messages API examples](api/messages/create.md) for more example code and parameter details.

### Example: One image

### Example: Multiple images

### Example: Multiple images with a system prompt

### Example: Four images across two conversation turns

---

##  Limitations

While Claude's image understanding capabilities are cutting-edge, there are some limitations to be aware of:

- **People identification**: Claude [cannot be used](https://www.anthropic.com/legal/aup) to name people in images and refuses to do so.
- **Accuracy**: Claude may hallucinate or make mistakes when interpreting low-quality, rotated, or very small images under 200 pixels.
- **Spatial reasoning**: Claude's coordinate and localization outputs are approximate. Follow the guidance in [Working with coordinates and bounding boxes](#working-with-coordinates-and-bounding-boxes) and verify outputs before relying on them.
- **Counting**: Claude can give approximate counts of objects in an image but may not always be precisely accurate, especially with large numbers of small objects.
- **AI generated images**: Claude does not know if an image is AI-generated and may be incorrect if asked. Do not rely on it to detect fake or synthetic images.
- **Inappropriate content**: Claude does not process inappropriate or explicit images that violate the [Acceptable Use Policy](https://www.anthropic.com/legal/aup).
- **Healthcare applications**: While Claude can analyze general medical images, it is not designed to interpret complex diagnostic scans such as CTs or MRIs. Claude's outputs should not be considered a substitute for professional medical advice or diagnosis.

Always carefully review and verify Claude's image interpretations, especially for high-stakes use cases. Do not use Claude for tasks requiring perfect precision or sensitive image analysis without human oversight.

---

##  FAQ

### What image file types does Claude support?

### Can Claude read image URLs?

### Is there a limit to the image file size I can upload?

### How many images can I include in one request?

### Does Claude read image metadata?

### Can I delete images I've uploaded?

### Where can I find details on data privacy for image uploads?

### What if Claude's image interpretation seems wrong?

### Can Claude generate or edit images?

---

##  Dive deeper into vision

Ready to start building with images using Claude? Here are a few helpful resources:

- [Multimodal cookbook](https://platform.claude.com/cookbook/multimodal-getting-started-with-vision): This cookbook has tips on [getting started with images](https://platform.claude.com/cookbook/multimodal-getting-started-with-vision) and [best practice techniques](https://platform.claude.com/cookbook/multimodal-best-practices-for-vision) to ensure the highest quality performance with images. See how you can effectively prompt Claude with images to carry out tasks such as [interpreting and analyzing charts](https://platform.claude.com/cookbook/multimodal-reading-charts-graphs-powerpoints) or [extracting content from forms](https://platform.claude.com/cookbook/multimodal-how-to-transcribe-text).
- [API reference](api/messages/create.md): Documentation for the Messages API, including example [API calls involving images](build-with-claude/working-with-messages.md).

If you have any other questions, reach out to the [support team](https://support.claude.com/). You can also join the [developer community](https://www.anthropic.com/discord) to connect with other creators and get help from Anthropic experts.

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
