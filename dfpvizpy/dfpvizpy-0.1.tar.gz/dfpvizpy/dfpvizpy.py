import os
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import matplotlib.font_manager as fm
from PIL import Image
from cycler import cycler

def append_images(images, direction='horizontal',
                  bg_color=(255,255,255), aligment='center'):
    """
    Appends images in horizontal/vertical direction.

    Args:
        images: List of PIL images
        direction: direction of concatenation, 'horizontal' or 'vertical'
        bg_color: Background color (default: white)
        aligment: alignment mode if images need padding;
           'left', 'right', 'top', 'bottom', or 'center'

    Returns:
        Concatenated image as a new PIL image object.
    """
    widths, heights = zip(*(i.size for i in images))

    if direction=='horizontal':
        new_width = sum(widths)
        new_height = max(heights)
    else:
        new_width = max(widths)
        new_height = sum(heights)

    new_im = Image.new('RGB', (new_width, new_height), color=bg_color)


    offset = 0
    for im in images:
        if direction=='horizontal':
            y = 0
            if aligment == 'center':
                y = int((new_height - im.size[1])/2)
            elif aligment == 'bottom':
                y = new_height - im.size[1]
            new_im.paste(im, (offset, y))
            offset += im.size[0]
        else:
            x = 0
            if aligment == 'center':
                x = int((new_width - im.size[0])/2)
            elif aligment == 'right':
                x = new_width - im.size[0]
            new_im.paste(im, (x, offset))
            offset += im.size[1]

    return new_im

def dfpSave(fname,g,fac=3.,despineX=False,despineY=False):
    try:
        isFacet = True
        axlist = list(g.axes.flat)
    except:
        axlist = list(g)
    
    if isFacet:
        try:
            plt.setp(g._legend.get_texts(),fontproperties=monserratReg)
            plt.setp(g._legend.get_title(),fontproperties=monserratReg)
            g._legend.draw_frame(False)
        except:
            pass

    for i,ax in enumerate(axlist):
        plt.sca(ax)
        try:
            plt.setp(ax.legend_.get_texts(),fontproperties=monserratReg)
            plt.setp(ax.legend_.get_title(),fontproperties=monserratReg)
            ax.legend_.draw_frame(False)
        except:
            pass

    
        plt.xticks(fontproperties=monserratThin)
        plt.yticks(fontproperties=monserratThin)
        ax.set_xlabel(ax.get_xlabel(),fontproperties=monserratReg)
        ax.set_ylabel(ax.get_ylabel(),fontproperties=monserratReg)
        ax.set_title (ax.get_title().upper(),fontproperties=futuraBold,fontsize=16)
        ax.title.set_fontsize(16)

        despine = [1,3]
        if despineX:
            ax.xaxis.set_ticks_position('none')
            despine.append(2)
            plt.xticks(fontproperties=monserratReg)
            ax.set_xlabel("")
        if despineY:
            ax.yaxis.set_ticks_position('none')
            despine.append(0)
            plt.yticks(fontproperties=monserratReg)
            ax.set_ylabel("")
        for j,spine in enumerate(ax.spines.values()):
            if j in despine:
                spine.set_edgecolor('None')
            else:
                spine.set_edgecolor(gray)
    plt.tight_layout()

    plt.savefig(fname)
    orig = Image.open(fname)
    width, height = orig.size

    #Create logo
    logo = Image.open(os.path.join(os.path.dirname(__file__),'dfp-line-logo-black.png'))
    lwidth, lheight = logo.size
    lwidth = int(lwidth/fac)
    lheight = int(lheight/fac)
    logo.thumbnail((lwidth,lheight),Image.ANTIALIAS)
    new_im = Image.new('RGB', (width, lheight+10),color=(255,255,255))
    new_im.paste(logo,(width-lwidth-20,5),logo)
    images = [Image.open(fname), new_im]
    combined = append_images(images, direction='vertical')
    combined.save(fname)
    plt.close()

plt.rcParams.update({'axes.titlesize': 'large'})
futuraBold      = fm.FontProperties(fname=os.path.join(os.path.dirname(__file__),'Futura Heavy font.ttf'))
monserratReg    = fm.FontProperties(fname=os.path.join(os.path.dirname(__file__),'Montserrat-Regular.ttf'))
monserratThin   = fm.FontProperties(fname=os.path.join(os.path.dirname(__file__),'Montserrat-Thin.ttf'))
gray = "#525353"
dfPal = sns.color_palette(["#124073","#A8BF14","#B71D1A","#BC4A11","#BF7A00","#b3b3b3","#000000"])
#dfPal = sns.color_palette(["#0a2645","#A8BF14","#B71D1A","#BC4A11","#BF7A00","#b3b3b3","#000000"])
sns.set_palette(dfPal)
for code, color in zip("bgrmyck", dfPal):
    rgb = mpl.colors.colorConverter.to_rgb(color)
    mpl.colors.colorConverter.colors[code] = rgb
    mpl.colors.colorConverter.cache[code] = rgb
plt.rc('axes', prop_cycle=(cycler('color', dfPal)))

