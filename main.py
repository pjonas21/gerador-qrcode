import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import SolidFillColorMask
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer


def generate_qrcode(data, back_color, front_color, file_name):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        color_mask=SolidFillColorMask(back_color=back_color, front_color=front_color)
    )

    image.save(f"{file_name}.png")


if __name__ == "__main__":
    generate_qrcode(
        "https://github.com/pjonas21",
        (0, 64, 105),
        (255, 255, 255),
        "qrcode"
    )