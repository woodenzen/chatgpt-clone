import os
import openai
import gradio as gr
from api_secret import API_KEY

#if you have OpenAI API key as an environment variable, enable the below
#openai.api_key = os.getenv("OPENAI_API_KEY")

#if you have OpenAI API key as a string, enable the below
openai.api_key = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..yd8oP2kosalAyxKv.yYocI7cN3GqQe8r858YTpbiQWZCEnQPbXcqJLOpcCz92Jixjh4sXABCy8qMp0yBxoPmhxW0o4DAiphBKp1sCtMw-ymLqaOJU8InwMjS2ve0D_S6zRQlmRjmwegTRX-RZ2RSoM-Py3rS0phGpar-ldbDsBzTMyFUhxg5FrlWfAmM9awq6IvldpPSp12qTZ7_sUoU_dPK6szE_HchRGDALH6O2BIzkybuINcpM9HRj9tI5UsXWFdPSraVIFKSRCLhXWIjIAK8QqRlFy5VUMbQ7YooLuluPUkAriTy0qwNwcn51TUvoCMaYWjZgY3Td24fslG6dA2n2y3d0KxHTYtDFpfa3XGKPf7YAgJPovnFu19qC0EXzJ7zl37rbiAGzUwrQaDuPegLEXG41LTJCdnhh_MpXfqvpPxBWUVmLtdhxWY_r9Ob2ho34_9ed3a68muonSizAzaUaSG2gGr0KgEd61L0SmGO325IbEanaiGy93j1MUD60b7Mo-pWxErGunuLGgv6JjvuXoWdvCvLREl5zxp7fBEBSbg6vv6_xxHHP-klHekyvcl3d1Voa40NeZ_Ik5C4DrQeMogyBnQxXD3lyYkdwhNIbD3Hmlmi93lDD18YldytnSKFDJS4K93vbisi5DQ9N_niNCg69ZtYlu_7f0_Vnx5MGuMxlbf8afeqE5AOv-5gBUuTUQrJMtg17AVbgd9ZUvKGa5k6Nnm8oa0q1LjSHJx7rFxKBpHKuoIhTgoJ0bkhD1fbVgE4CkU30UY0iCUNAKlw3ZnOSCLOESsT3K52WDWbeJc1B7D_0xxnbc9fnNBQ1eG3d9Xc98foL_QqEqj2tbF8iqaYvB5gSxtlMMnq0qrhBDdJLj90KFKHHNAaO36naZHJBaYs4UZZZ2aN5K_sBwENCGzb46euVnyrnJi5fiZ0mAMU7RG_7uH3ZboS5QKfTFGzX2ekd2d0EdTgIVHykjngV4g1VItXiAFCiWoUvbYIBNTxARQFk0U73ojHWNlA5-BkCKQRCwopJgvZW7qqf86-z6IC7B7Utf2pRv51HLGnmLEjeHh4fkqN7NlB6PE_sTsZzWQTu3YNsZId7AuThtIuQkBWhSzSZ7w6DarJBQ8OWDn5gaPav0AMs59AA24eTHTlNVnVRibvX1WcRKFazaeotnn9SjrhmFHekN0cd9mhAWEpntEeODQ1j0YdD9QEQY5Paqqz4wsSxFB5b2cu3_gsrtzMwUAPqQRNBBujseP7KF8iQNLFpmEMe5P8lpFPIC-KKlfwoYu0LB_XL6E9shW37u8KYpzlutFiN2f-RC25SnBu_JKp7JW53d9iZE-79wFOnKPp1mIGu3_aQBUOgo3XLQoIDIxdJi81mnD8CEhmbTAqK6SD43JSFHWMZRBdkeRChEoCIVYDbqMa7JtomSNNax7MKVWzH6NiYBXL89KwYm2R6XiXrMo23ZIaJw7OWsfZU5bWGH4yNQvEt0z2z_x1yNBgYKk4wulhl9yCACObkIQVs9Ov284Wy91X45D30_bVJzy90BTuEC1eu5Y-O4lebOkPyr3W15RH5A3r5GvYrNG-RhmZoVyoAg7Uiwf9FExGFruilXt35eAU6TyWEMIiaqYyzpeRFW0_hFSmYR3Dzf48ibc4G1h4XOun5amstSD1gZblFMHMmzAc6i8hdcM8gSM7R-UTFALwzZ32dhQBOPSuLiA4Dz3Y11BQKDYaVZn49CrXKfTQP-tsKcOMrLHtMjJMci6YzNzRWS8PBrtZuppPBBz6KxteyRxBYTDzgM6daA6NH7LlSb3MfRnH57VdUsUjPsAZDWMoiD_ozkcUoA5mGl0BZdjhMbaMBR2ksxcqJ73qhjO725u55VJt0N37SSPt9E6p7pDS2WljFIkaKWWyQaw8SdfpvXZHXp1OybVByg5V1OGaWj0Bdr2xcbpVVWo2fnHPOIkH3sY4O4B9QawAayVjdpyDHI6WjQql2Dbk0u7vaKNLojfscL-m40vUhIzMshRWqD7jLvc7AUPG4TnmAqbh7y2mnvV0lAm4-oQKJ0GaRZGcNDIeNFpki0W-kBTjqQ74dzSya1vuAi07XNuI3rY6cvvMBK2VBsDZvrZnTUwZTJRT8LwS1DLSbghQ6YLJpuy__nELrnBMITQ7mIosHp3e2RH34i-LjR43VRaJD13JCcf-TETprEZYKVtSSW1wbZPiEm4KRfkjkVjfsA4ibrFQBdIfKy2m6hKvRMsN6-TAuQA6ano3QmVGArMVKjU0c2ycws33gvIG_Tk3b-a7Az3dX-Ua2nw-37MjAl-NIqC5crI9t9AI9DSX7fWEPA5HzN8IJxLCt0T9y8_ZDGatxSD5XpBguWmBVhtqJYKxdk2tJIcJYI-axwUIRBFl54qwjLps1hKEtR0rbTQsRVGZCo60zk_hQuyLiuv8X28E0N0j2S5QQeIAD8Hg7DlJlVsHtPsxgTVwxfc22Cm0L9UTyi-A.oM1V9ZYlFakbKmzLWV7EEA"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>Build Yo'own ChatGPT with OpenAI API & Gradio</center></h1>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True)
