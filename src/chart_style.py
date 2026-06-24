import matplotlib.pyplot as plt
# CÁC BIẾN MÀU SẮC VÀ PHONG CÁCH CHO BIỂU ĐỒ
from numpy import blackman
blue_color = (29/255, 66/255, 137/255)
gray_color = (166/255, 166/255, 166/255)
text_color = "#ac0450"
blue_color = (29/255, 66/255, 137/255)
red_color = (192/255, 80/255, 77/255)
yellow_color = (250/255, 192/255, 144/255)
colors = ["#920042", "#aa095b", "#c52b7e", "#ed92bb", "#e1687f"]
color_cot = ["#ec60a2", "#A6004B", "#ec60a2", "#ec60a2", "#ec60a2", "#ffbcde"]
my_pink = "#cd6a77"

# --- 1. CẤU HÌNH FONT HỆ THỐNG ---
# Thiết lập Times New Roman làm font mặc định
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']

# --- 2. CÁC HÀM TÙY CHỈNH THEO YÊU CẦU ---

def set_title(ax, _title: str, fontname: str = 'Times New Roman', fontsize: int = 16, color: str = 'black'):
    """Thiết lập tiêu đề font Times New Roman, màu đen."""
    ax.set_title(
        _title,
        fontdict={'fontname': fontname, 'fontsize': fontsize, 'color': color, 'weight': 'bold'},
        pad=20
    )
    return ax

def set_label(ax, xlabel: str, ylabel: str, fontname: str = 'Times New Roman', fontsize: int = 14, labelsize: int = 10, color: str = 'black'):
    """Nhãn trục (chữ) lớn hơn, số (tick labels) nhỏ hơn, tất cả màu đen."""
    text_props = {'fontname': fontname, 'fontsize': fontsize, 'color': color}
    
    # Thiết lập nhãn trục
    ax.set_xlabel(xlabel, fontname=fontname, fontsize=fontsize, color=color, labelpad=15)
    ax.set_ylabel(ylabel, fontname=fontname, fontsize=fontsize, color=color, labelpad=15)

    # Thiết lập số trên trục (ticks)
    ax.tick_params(axis='both', labelsize=labelsize, colors=color)
    
    # Đảm bảo các con số cũng dùng font Times New Roman
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
        label.set_fontname(fontname)
        label.set_fontsize(labelsize)
    return ax

def set_legend(ax, loc: str = 'best', fontsize: int = 10, fontname: str = 'Times New Roman', _text_color: str = 'black'):
    """Chú thích không khung, font Times New Roman màu đen."""
    legend = ax.legend(loc=loc, fontsize=fontsize, frameon=False)
    if legend:
        for text in legend.get_texts():
            text.set_fontname(fontname)
            text.set_color(_text_color)
    return ax

def set_spines(ax, spines: list = ['top', 'right']):
    """Ẩn spines chỉ định, các spines còn lại màu đen."""
    valid_spines = {'top', 'right', 'left', 'bottom'}
    for key in spines:
        if key in valid_spines:
            ax.spines[key].set_visible(False)
    
    # Những đường còn lại (trái, dưới) để màu đen
    for key in (valid_spines - set(spines)):
        ax.spines[key].set_color('black')
    return ax

def convert_rect(fig, linewidth: float = 1.0):
    """Vẽ khung viền đen bao quanh toàn bộ hình ảnh."""
    rect = plt.Rectangle((0, 0), 1, 1,
                        transform=fig.transFigure,
                        color='black',
                        linewidth=linewidth,
                        fill=False,
                        clip_on=False)
    fig.patches.append(rect)
    return fig