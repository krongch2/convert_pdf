import os
import pdf2image
import img2pdf

def pdf2pngs(pdf_name):
    '''
    Converts PDF and stores the output PNGs in the folder with the same name as PDF
    '''
    prefix, ext = os.path.splitext(pdf_name)
    imgs = pdf2image.convert_from_path(pdf_name)
    os.makedirs(prefix, exist_ok=True)
    max_page = str(len(imgs))
    pad = len(max_page)
    for i, img in enumerate(imgs):
        png_name = f'{prefix}/{i+1:0{pad}}.png'
        img.save(png_name)

def pngs2pdf(png_dir):
    '''
    Converts a list of PNGs to PDF with the same name as the provided folder `png_dir`
    '''
    fns = [f'{png_dir}/{fn}' for fn in os.listdir(png_dir) if fn.endswith('.png')]
    fns_str = ' '.join(fns)
    os.system(f'img2pdf {fns_str} -o {png_dir}.pdf')

if __name__ == '__main__':
    pdf2pngs('test.pdf')
    # pngs2pdf('test')
