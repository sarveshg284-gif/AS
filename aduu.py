import streamlit as st
import random

st.set_page_config(
    page_title="Virtual Gift",
    page_icon="💖",
    layout="centered"
)

# ---------- CSS ----------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#ffe6ea,#ffd6e8,#fff0f5);
}

.main{
    text-align:center;
}

.title{
    font-size:40px;
    font-weight:bold;
    color:#ff1493;
    margin-bottom:20px;
    animation:pulse 1.5s infinite;
}

.message{
    font-size:28px;
    color:#444;
    margin-top:20px;
}

.gift{
    font-size:90px;
    animation:bounce 1.2s infinite;
}

.special{
    background:white;
    padding:20px;
    border-radius:20px;
    box-shadow:0 0 20px rgba(255,105,180,.4);
    margin-top:20px;
}

@keyframes bounce{
    0%,100%{transform:translateY(0);}
    50%{transform:translateY(-15px);}
}

@keyframes pulse{
    0%{transform:scale(1);}
    50%{transform:scale(1.08);}
    100%{transform:scale(1);}
}

.floating-heart{
    position:fixed;
    font-size:25px;
    animation:floatUp 8s linear infinite;
    opacity:.7;
}

@keyframes floatUp{
    from{
        transform:translateY(100vh);
    }
    to{
        transform:translateY(-100px);
    }
}

</style>
""", unsafe_allow_html=True)

# ---------- Floating Hearts ----------
hearts_html = ""

for i in range(20):
    hearts_html += f"""
    <div class="floating-heart"
         style="left:{random.randint(0,95)}%;
         animation-delay:{random.random()*5}s;">
         💖
    </div>
    """

st.markdown(hearts_html, unsafe_allow_html=True)

# ---------- Session State ----------
if "show_gift" not in st.session_state:
    st.session_state.show_gift = False

if "reveal" not in st.session_state:
    st.session_state.reveal = False

# ---------- Main UI ----------
st.markdown(
    '<div class="title">💖 Do You Love Me?? 💖</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    if st.button("YES !! ❤️", use_container_width=True):
        st.session_state.show_gift = True
        st.balloons()

with col2:
    funny_texts = [
        "NO 😅",
        "Try Again 😜",
        "Wrong Button 😂",
        "Not Allowed 😆",
        "Think Again 🤭"
    ]

    st.button(
        random.choice(funny_texts),
        use_container_width=True
    )

# ---------- Gift Section ----------
if st.session_state.show_gift:

    st.markdown(
        '<div class="message">I know you love me 💕</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="gift">🎁 🎁 🎁</div>',
        unsafe_allow_html=True
    )

    if st.button("🎀 Tap To Reveal Gifts 🎀"):

        st.session_state.reveal = True
        st.balloons()

# ---------- Reveal ----------
if st.session_state.reveal:

    st.markdown("""
    <div class="special">

    <h1>🌸 Here Is Your Gift 🌸</h1>

    <h2>You Are Special ❤️</h2>

    <div style="font-size:80px;">
    💐 🧸 🍫
    </div>

    <br>

    <h3 style="color:#ff1493;">
    Thank You For Being Amazing 💖
    </h3>

    </div>
    """, unsafe_allow_html=True)

    st.success("🎉 Surprise Unlocked!")
