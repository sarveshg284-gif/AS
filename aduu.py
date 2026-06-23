import streamlit as st

st.set_page_config(
    page_title="Virtual Gift 💖",
    page_icon="💖",
    layout="centered"
)

if "show_gift" not in st.session_state:
    st.session_state.show_gift = False

st.markdown(
    """
    <h1 style='text-align:center;color:#ff1493;'>
        💖 Do You Love Me?? 💖
    </h1>
    """,
    unsafe_allow_html=True
)

# YES Button
if st.button("YES !! ❤️"):
    st.session_state.show_gift = True
    st.balloons()

# Moving NO Button
st.markdown(
"""
<div style="position:relative;height:250px;">
<button id="noBtn">
        NO 😜
    </button>

</div>

<style>


noBtn{
    position:absolute;
    left:50%;
    top:80px;
    transform:translateX(-50%);
    background:#ff4da6;
    color:white;
    border:none;
    padding:14px 30px;
    border-radius:30px;
    font-size:20px;
    font-weight:bold;
    cursor:pointer;
    box-shadow:0 5px 15px rgba(0,0,0,.2);
    transition:0.15s;
    animation:shake 0.8s infinite;
}

@keyframes shake{
    0%{transform:translateX(-50%) rotate(0deg);}
    25%{transform:translateX(-50%) rotate(3deg);}
    50%{transform:translateX(-50%) rotate(-3deg);}
    75%{transform:translateX(-50%) rotate(2deg);}
    100%{transform:translateX(-50%) rotate(0deg);}
}

</style>

<script>

const texts = [
    "NO 😜",
    "Try Again 😂",
    "Wrong Button 🤣",
    "Not Today 😆",
    "Catch Me 😎",
    "Impossible 😝"
];

const btn = document.getElementById("noBtn");

btn.addEventListener("mouseover", () => {

    const maxX = window.innerWidth - 180;
    const maxY = 220;

    btn.style.left = Math.random() * maxX + "px";
    btn.style.top = Math.random() * maxY + "px";

    btn.innerHTML =
        texts[Math.floor(Math.random()*texts.length)];
});

</script>
""",
unsafe_allow_html=True
)

# Gift Section
if st.session_state.show_gift:
    st.markdown(
        """
        <div style="
            background:white;
            padding:25px;
            border-radius:20px;
            text-align:center;
            box-shadow:0 0 20px rgba(255,105,180,.4);
            margin-top:20px;
        ">

        <h2>💕 I knew it! 💕</h2>

        <div style="font-size:90px;">
            🎁 🎁 🎁
        </div>

        <h3>🌸 Here is your gift 🌸</h3>

        <div style="font-size:70px;">
            💐 🧸 🍫
        </div>

        <p style="font-size:24px;color:#ff1493;">
            You Are Special ❤️
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )
