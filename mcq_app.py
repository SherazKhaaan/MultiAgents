"""
MCQ Quiz App — Streamlit UI for revision MCQs.
Loads JSON files from ./<Module>/mcqs/Week<N>_mcqs.json
Run with: streamlit run mcq_app.py
"""
import json
import glob
import os
import streamlit as st

st.set_page_config(
    page_title="Revision MCQs",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* Question card */
.q-card {
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 20px 24px;
    margin-bottom: 20px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
}
.q-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 6px;
}
.q-num { font-weight: 700; color: #3b82f6; font-size: 0.88rem; }
.q-src { font-size: 0.78rem; color: #94a3b8; font-style: italic; }
.badge-correct { background:#dcfce7; color:#16a34a; padding:2px 10px; border-radius:12px; font-weight:700; font-size:0.85rem; }
.badge-partial  { background:#fef9c3; color:#ca8a04; padding:2px 10px; border-radius:12px; font-weight:700; font-size:0.85rem; }
.badge-wrong    { background:#fee2e2; color:#dc2626; padding:2px 10px; border-radius:12px; font-weight:700; font-size:0.85rem; }
/* Option feedback rows */
.opt-correct-selected { background:#dcfce7; color:#14532d; border-left:4px solid #22c55e; padding:8px 12px; border-radius:6px; margin:4px 0; }
.opt-correct-missed   { background:#fff; color:#14532d; border:2px dashed #22c55e; padding:8px 12px; border-radius:6px; margin:4px 0; }
.opt-wrong-selected   { background:#fee2e2; color:#7f1d1d; border-left:4px solid #ef4444; padding:8px 12px; border-radius:6px; margin:4px 0; }
.opt-neutral          { background:#f8fafc; color:#1e293b; border-left:4px solid #e2e8f0; padding:8px 12px; border-radius:6px; margin:4px 0; }
/* Explanation items */
.exp-correct { border-left:3px solid #22c55e; background:#f0fdf4; color:#14532d; padding:10px 14px; border-radius:6px; margin:6px 0; font-size:0.92rem; }
.exp-wrong   { border-left:3px solid #ef4444; background:#fef2f2; color:#7f1d1d; padding:10px 14px; border-radius:6px; margin:6px 0; font-size:0.92rem; }
.notes-quote { font-style:italic; color:#334155; background:#f1f5f9; padding:2px 6px; border-radius:3px; }
.ref-tag     { font-size:0.8rem; color:#3b82f6; font-weight:500; }
/* Section heading */
.section-heading { color:#1e40af; border-bottom:2px solid #dbeafe; padding-bottom:6px; margin:28px 0 16px; }
</style>
""", unsafe_allow_html=True)


# ── Data loading ────────────────────────────────────────────────────────────

@st.cache_data
def discover_files():
    """Return dict: {module: {week_num: path}}"""
    pattern = os.path.join(os.path.dirname(__file__), "*", "mcqs", "Week*_mcqs.json")
    found: dict[str, dict[int, str]] = {}
    for path in sorted(glob.glob(pattern)):
        parts = path.replace("\\", "/").split("/")
        # …/ModuleName/mcqs/WeekN_mcqs.json
        module = parts[-3]
        filename = parts[-1]  # WeekN_mcqs.json
        week_str = filename.replace("Week", "").replace("_mcqs.json", "")
        try:
            week_num = int(week_str)
        except ValueError:
            continue
        found.setdefault(module, {})[week_num] = path
    return found


@st.cache_data
def load_quiz(path: str) -> dict:
    with open(path, "r", encoding="utf-8-sig") as f:
        return json.load(f)


# ── Session state helpers ───────────────────────────────────────────────────

def state_key(quiz_id: str, q_id: str, suffix: str) -> str:
    return f"{quiz_id}__{q_id}__{suffix}"


def init_question_state(quiz_id: str, q_id: str, options: list[dict]):
    for opt in options:
        k = state_key(quiz_id, q_id, f"cb_{opt['letter']}")
        if k not in st.session_state:
            st.session_state[k] = False
    checked_key = state_key(quiz_id, q_id, "checked")
    if checked_key not in st.session_state:
        st.session_state[checked_key] = False


def reset_quiz(quiz_id: str, data: dict):
    for section in data["sections"]:
        for q in section["questions"]:
            for opt in q["options"]:
                k = state_key(quiz_id, q["id"], f"cb_{opt['letter']}")
                st.session_state[k] = False
            st.session_state[state_key(quiz_id, q["id"], "checked")] = False


def get_score(quiz_id: str, data: dict) -> tuple[int, int, int]:
    """Return (correct, answered, total)"""
    total = sum(len(s["questions"]) for s in data["sections"])
    answered = 0
    correct = 0
    for section in data["sections"]:
        for q in section["questions"]:
            if st.session_state.get(state_key(quiz_id, q["id"], "checked"), False):
                answered += 1
                selected = {
                    opt["letter"]
                    for opt in q["options"]
                    if st.session_state.get(state_key(quiz_id, q["id"], f"cb_{opt['letter']}"), False)
                }
                if selected == set(q["correct"]):
                    correct += 1
    return correct, answered, total


# ── Rendering ───────────────────────────────────────────────────────────────

def render_question(quiz_id: str, q: dict, q_index: int):
    q_id = q["id"]
    checked_key = state_key(quiz_id, q_id, "checked")
    is_checked = st.session_state.get(checked_key, False)

    correct_set = set(q["correct"])
    selected_set = {
        opt["letter"]
        for opt in q["options"]
        if st.session_state.get(state_key(quiz_id, q_id, f"cb_{opt['letter']}"), False)
    }

    # Determine result badge
    if is_checked:
        if selected_set == correct_set:
            badge = '<span class="badge-correct">✓ Correct</span>'
        elif selected_set & correct_set:
            badge = '<span class="badge-partial">~ Partial</span>'
        else:
            badge = '<span class="badge-wrong">✗ Incorrect</span>'
    else:
        badge = ""

    st.markdown(
        f'<div class="q-header">'
        f'<span class="q-num">Question {q_index}</span>'
        f'<span class="q-src">{q.get("source_ref","")}</span>'
        f'{badge}'
        f'</div>',
        unsafe_allow_html=True,
    )

    # Question text — use st.markdown so KaTeX (via streamlit) renders math
    st.markdown(q["text"])

    # Options — one checkbox per option
    for opt in q["options"]:
        cb_key = state_key(quiz_id, q_id, f"cb_{opt['letter']}")
        letter = opt["letter"]

        if is_checked:
            is_correct = letter in correct_set
            is_selected = letter in selected_set
            if is_correct and is_selected:
                css_class = "opt-correct-selected"
                icon = "✅"
            elif is_correct and not is_selected:
                css_class = "opt-correct-missed"
                icon = "⬜ (missed)"
            elif not is_correct and is_selected:
                css_class = "opt-wrong-selected"
                icon = "❌"
            else:
                css_class = "opt-neutral"
                icon = ""

            st.markdown(
                f'<div class="{css_class}"><strong>{icon} {letter}.</strong> {opt["text"]}</div>',
                unsafe_allow_html=True,
            )
        else:
            # Render as checkbox with letter prefix
            label = f"**{letter}.** {opt['text']}"
            st.checkbox(label, key=cb_key, disabled=False)

    # Check Answer / result
    if not is_checked:
        if st.button("Check Answer", key=f"btn_{quiz_id}_{q_id}"):
            st.session_state[checked_key] = True
            st.rerun()
    else:
        # Feedback message
        if selected_set == correct_set:
            st.success("Correct! All answers right.")
        elif selected_set & correct_set:
            missed = correct_set - selected_set
            wrong = selected_set - correct_set
            parts = []
            if wrong:
                parts.append(f"Wrong selections: {', '.join(sorted(wrong))}")
            if missed:
                parts.append(f"Missed: {', '.join(sorted(missed))}")
            st.warning("Partially correct. " + " | ".join(parts))
        else:
            correct_letters = ", ".join(sorted(correct_set))
            st.error(f"Incorrect. Correct answer(s): {correct_letters}")

        # Explanations in expander
        if q.get("explanations"):
            with st.expander("Show detailed explanation"):
                for exp in q["explanations"]:
                    css_class = "exp-correct" if exp["is_correct"] else "exp-wrong"
                    icon = "✓" if exp["is_correct"] else "✗"
                    quote_html = (
                        f' — <span class="notes-quote">"{exp["notes_quote"]}"</span>'
                        if exp.get("notes_quote")
                        else ""
                    )
                    st.markdown(
                        f'<div class="{css_class}">'
                        f'<strong>{icon} {exp["letter"]} {"is correct" if exp["is_correct"] else "is incorrect"}.</strong> '
                        f'{exp["text"]} '
                        f'<span class="ref-tag">{exp.get("section_ref","")}</span>'
                        f'{quote_html}'
                        f'</div>',
                        unsafe_allow_html=True,
                    )

    st.markdown("---")


def render_quiz(quiz_id: str, data: dict):
    # Init all question states
    for section in data["sections"]:
        for q in section["questions"]:
            init_question_state(quiz_id, q["id"], q["options"])

    # Header metrics
    correct, answered, total = get_score(quiz_id, data)
    remaining = total - answered
    pct = int(answered / total * 100) if total > 0 else 0

    col1, col2, col3 = st.columns(3)
    col1.metric("✓ Correct", f"{correct}/{answered}")
    col2.metric("📋 Answered", f"{answered}/{total}")
    col3.metric("⏳ Remaining", remaining)
    st.progress(pct / 100, text=f"{pct}% complete")

    if st.button("🔄 Reset All Answers", key=f"reset_{quiz_id}"):
        reset_quiz(quiz_id, data)
        st.rerun()

    st.markdown("---")

    # Render sections + questions
    q_index = 1
    for section in data["sections"]:
        st.markdown(f'<h2 class="section-heading">{section["title"]}</h2>', unsafe_allow_html=True)
        for q in section["questions"]:
            render_question(quiz_id, q, q_index)
            q_index += 1


# ── Main app ────────────────────────────────────────────────────────────────

def main():
    files = discover_files()

    if not files:
        st.title("📚 Revision MCQs")
        st.warning(
            "No MCQ files found. Run `/generate-mcqs <Module>` to generate them.\n\n"
            "Expected path format: `<Module>/mcqs/Week<N>_mcqs.json`"
        )
        return

    with st.sidebar:
        st.title("📚 Revision MCQs")
        st.markdown("---")

        modules = sorted(files.keys())
        module = st.selectbox("Module", modules)

        weeks = sorted(files[module].keys())
        week_labels = {w: f"Week {w}" for w in weeks}
        week = st.selectbox("Week", weeks, format_func=lambda w: week_labels[w])

        st.markdown("---")
        st.caption("Generated by `/generate-mcqs`")

    path = files[module][week]
    data = load_quiz(path)
    quiz_id = f"{module}_w{week}"

    st.title(f"Week {data['week']}: {data['title']}")
    st.caption(f"Module: {data['module']} · {sum(len(s['questions']) for s in data['sections'])} questions")
    st.markdown("---")

    render_quiz(quiz_id, data)


if __name__ == "__main__":
    main()
