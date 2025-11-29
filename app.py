import math

import streamlit as st


st.set_page_config(
    page_title="Hàm lượng nhựa tưới - TCVN 8863:2011",
    page_icon="🛣️",
    layout="wide",
)


@st.cache_data
def format_number(value: float, digits: int = 2) -> str:
    """Format number using Vietnamese separators."""
    if math.isnan(value):
        return "N/A"
    formatted = f"{value:,.{digits}f}"
    parts = formatted.split(".")
    if len(parts) == 2:
        integer_part = parts[0].replace(",", ".")
        decimal_part = parts[1]
        return f"{integer_part},{decimal_part}"
    return parts[0].replace(",", ".")


def compute_binder_rate(mass_g: float, area_cm2: float) -> dict[str, float]:
    """Compute spray rate from tray mass result."""
    if mass_g <= 0 or area_cm2 <= 0:
        return {
            "rate_g_cm2": float("nan"),
            "rate_kg_m2": float("nan"),
        }

    rate_g_cm2 = mass_g / area_cm2
    rate_kg_m2 = rate_g_cm2 * 10  # 1 g/cm2 = 10 kg/m2
    return {
        "rate_g_cm2": rate_g_cm2,
        "rate_kg_m2": rate_kg_m2,
    }


def evaluate_spec(rate_kg_m2: float, spec_min: float) -> str:
    """Provide quick compliance message."""
    if math.isnan(rate_kg_m2):
        return "Thiếu dữ liệu."
    if rate_kg_m2 >= spec_min:
        return "Đạt yêu cầu."
    return "Thiếu nhựa so với yêu cầu, cần tăng lưu lượng."


def compute_tray_area(length_cm: float, width_cm: float) -> float:
    """Rectangle tray area in cm²."""
    if length_cm <= 0 or width_cm <= 0:
        return float("nan")
    return length_cm * width_cm


def main() -> None:
    st.title("Hàm lượng nhựa tưới theo TCVN 8863:2011")
    st.caption(
        "Xác định lưu lượng tưới nhựa nóng bằng phương pháp khay cân theo tiêu chuẩn "
        "TCVN 8863:2011 - Mặt đường láng nhựa nóng."
    )

    with st.sidebar:
        try:
            st.image("logo.png", use_container_width=True)
        except FileNotFoundError:
            st.warning("Không tìm thấy file logo.png")

        st.markdown(
            "<div style='text-align: center; margin-top: 10px; margin-bottom: 10px;'>"
            "<h4>CÔNG TY TỨ HỮU</h4>"
            "<p style='font-size: 0.9em; color: #666;'>Tác giả: MR Tuấn - 0946135156</p>"
            "</div>",
            unsafe_allow_html=True,
        )
        st.divider()

        st.header("Hướng dẫn nhanh")
        st.markdown(
            "- Làm sạch khay trước khi cân.\n"
            "- Cân khay rỗng và khay + nhựa, ghi số tới ±0,1 g.\n"
            "- Đo chiều dài, chiều rộng khay để tính diện tích (cm²).\n"
            "- Nhập giới hạn tối thiểu của thiết kế để so sánh."
        )

    st.subheader("1. Khối lượng khay và nhựa")
    col1, col2 = st.columns(2)
    mass_full = col1.number_input(
        "Khối lượng khay + nhựa (g)",
        min_value=0.0,
        value=1100.0,
        step=0.1,
    )
    mass_empty = col2.number_input(
        "Khối lượng khay rỗng (g)",
        min_value=0.0,
        value=855.0,
        step=0.1,
    )
    mass_g = mass_full - mass_empty
    if mass_g <= 0:
        st.error("Khối lượng nhựa thu được phải lớn hơn 0 g.")
    else:
        st.info(f"Khối lượng nhựa tính được: **{format_number(mass_g, 2)}** g")

    st.subheader("2. Diện tích khay (hình chữ nhật)")
    col_dim1, col_dim2 = st.columns(2)
    length_cm = col_dim1.number_input(
        "Chiều dài khay (cm)",
        min_value=0.0,
        value=40.0,
        step=0.5,
    )
    width_cm = col_dim2.number_input(
        "Chiều rộng khay (cm)",
        min_value=0.0,
        value=25.0,
        step=0.5,
    )
    area_cm2 = compute_tray_area(length_cm, width_cm)
    if math.isnan(area_cm2):
        st.error("Diện tích khay phải lớn hơn 0 cm².")
    else:
        st.info(
            f"Diện tích khay = {format_number(length_cm, 1)} × "
            f"{format_number(width_cm, 1)} = {format_number(area_cm2, 1)} cm²"
        )

    st.subheader("3. Yêu cầu thiết kế / tiêu chuẩn")
    spec_min = st.number_input(
        "Giới hạn tối thiểu (kg/m²)",
        min_value=0.0,
        value=1.2,
        step=0.1,
    )

    results = compute_binder_rate(mass_g, area_cm2)
    rate_status = evaluate_spec(results["rate_kg_m2"], spec_min)

    if math.isnan(results["rate_kg_m2"]):
        st.error("Vui lòng nhập khối lượng và diện tích hợp lệ để tính hàm lượng nhựa.")
    else:
        st.success("Đã tính xong hàm lượng nhựa tưới cho khay hiện tại.")
        st.metric(
            "Hàm lượng nhựa (kg/m²)",
            format_number(results["rate_kg_m2"], 2),
        )
        st.info(rate_status)

    st.caption(
        "Ghi chú: TCVN 8863:2011 yêu cầu hàm lượng nhựa nằm trong dải thiết kế, "
        "cần kiểm tra định kỳ bằng khay cân để điều chỉnh vòi tưới kịp thời."
    )


if __name__ == "__main__":
    main()

