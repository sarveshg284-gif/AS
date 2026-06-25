import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Virtual Love Game 💖",
    page_icon="💖",
    layout="centered"
)

if "show_gift" not in st.session_state:
    st.session_state.show_gift = False


# Title
st.markdown("<h1 style='text-align:center;color:red;'>💭 A Message for You 💭</h1>", unsafe_allow_html=True)
st.markdown("""
<p style='text-align:center;font-size:18px;color:#333;line-height:1.8;'>
    Before I met you, I never knew what it was like to smile 😊 for no reason.<br>
    Now that you're here, I think my entire life will fall into place.☺️🫶
</p>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align:center;font-size:18px;color:#333;line-height:1.8;'>
   I don't know how much you love me, but I love you with all my heart."❤️🤌🙂<br>
</p>
""", unsafe_allow_html=True)
st.markdown(
    """
    <h2 style='text-align:center;color:#ff1493;'>
        💖 Will you be mine 💗🫴 💖
    </h2>
    """,
    unsafe_allow_html=True
)

# YES BUTTON
if st.button("YES !! ❤️"):
    st.session_state.show_gift = True
    st.balloons()


# HTML GAME (NO button runs away)
components.html(
"""
<!DOCTYPE html>
<html>
<head>
<style>

body{
    margin:0;
    overflow:hidden;
    background:transparent;
}

#noBtn{
    position:absolute;
    top:120px;
    left:55%;
    transform:translateX(-50%);
    background:#ff4da6;
    color:white;
    border:none;
    padding:14px 28px;
    border-radius:30px;
    font-size:18px;
    cursor:pointer;
    transition:0.1s;
    box-shadow:0 5px 15px rgba(0,0,0,0.2);
}

#yesFake{
    display:none;
}

</style>
</head>

<body>

<button id="noBtn">NO 😜</button>

<script>

const btn = document.getElementById("noBtn");

const texts = [
    "NO 😜",
    "Try Again 😂",
    "Wrong Button 🤣",
    "Catch Me 😎",
    "Impossible 😝",
    "Not Today 😆"
];

btn.addEventListener("mouseover", () => {

    const maxX = window.innerWidth - 150;
    const maxY = window.innerHeight - 150;

    btn.style.left = Math.random() * maxX + "px";
    btn.style.top = Math.random() * maxY + "px";

    btn.innerHTML = texts[Math.floor(Math.random()*texts.length)];
});

</script>

</body>
</html>
""",
height=250
)


# GIFT SECTION
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

        <h3>💕 I knew it! 💕</h3>

        <div style="font-size:90px;">
            🎁 🎁 🎁
        </div>

        <h4>🌸 Here is your gift 🌸</h4>

        <div style="font-size:70px;">
            💐 🧸 🍫
        </div>
        st.markdown("""
<p style='text-align:center;font-size:18px;color:#333;line-height:1.8;'>
   I don't know how much you love me, but I love you with all my heart."❤️🤌🙂<br>
</p>
""", unsafe_allow_html=True)
       
        <p style="font-size:22px;color:#ff1493;">
            You are special ❤️
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )
