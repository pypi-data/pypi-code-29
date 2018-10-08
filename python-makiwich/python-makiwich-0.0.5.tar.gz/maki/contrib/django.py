from django.http import HttpResponse, Http404

from maki import MakiMarker


def maki_icon(request, name):
    """
    Django view to serve icons.

    Usage:

        path("maki_icon/<str:name>", maki_icon, name="maki_icon")

    Name parameter must be of the following format, size, icon_name and color are optional:

        (pin-s|pin-l)-<label>+<color>(@2x)?.(png|svg)

    Some examples of valid names:

        pin-s-beer+fff.png
        pin-s-beer+f0f.png
        pin-l-park+3388ff.png
        pin-l-park-alt1+3388ff.png
        pin-l-park-alt1+3388ff@2x.png
        pin-l-park.png
        pin-l.png
        pin-l@2x.png
    """
    if not name[:5] in ["pin-s", "pin-l"]:
        raise Http404("Marker name must start with pin-s or pin-l")

    kwargs = {"size": name[4]}
    if not name[-3:] in ["svg", "png"]:
        raise Http404("Format must be png or svg")

    remainder = name[5:-4]
    pngkwargs = {}
    if remainder.endswith("@2x"):
        if name.endswith(".svg"):
            raise Http404("@2x suffix only valid for png.")
        pngkwargs["scale"] = 2
        remainder = remainder[:-3]

    remainder = remainder.strip("-")

    if "+" in remainder:
        symbol, tint = remainder.split("+")
        kwargs["symbol"] = symbol
        kwargs["tint"] = tint
    elif remainder == "":
        pass
    else:
        kwargs["symbol"] = remainder

    # print(kwargs)
    icon = MakiMarker(**kwargs)
    return HttpResponse(icon.png(**pngkwargs) if name.endswith("png") else icon.svg())
