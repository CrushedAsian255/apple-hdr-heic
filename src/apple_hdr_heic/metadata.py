from exiftool import ExifToolHelper


class AppleHDRMetadata:
    __slots__ = ["maker33", "maker48", "profile_desc", "hdrgainmap_version", "aux_type"]

    def __init__(self, file_name):
        for attr in self.__slots__:
            setattr(self, attr, None)
        # we are primarily interested in maker tags 33 (0x0021) and 48 (0x0030)
        # see https://github.com/exiftool/exiftool/blob/405674e0/lib/Image/ExifTool/Apple.pm
        tag_patterns = ["XMP:HDR*", "Apple:HDR*", "ICC_Profile:ProfileDesc*", "Quicktime:Auxiliary*"]
        with ExifToolHelper() as et:
            tags = et.get_tags(file_name, tags=tag_patterns)[0]
            for tag, val in tags.items():
                if tag == "XMP:HDRGainMapVersion":
                    self.hdrgainmap_version = val
                elif tag == "MakerNotes:HDRHeadroom":
                    self.maker33 = val
                elif tag == "MakerNotes:HDRGain":
                    self.maker48 = val
                elif tag == "ICC_Profile:ProfileDescription":
                    self.profile_desc = val
                elif tag == "Quicktime:AuxiliaryImageType":
                    self.aux_type = val

    @property
    def headroom(self) -> float:
        # ref https://developer.apple.com/documentation/appkit/images_and_pdf/applying_apple_hdr_effect_to_your_photos
        assert self.maker33 is not None and self.maker48 is not None
        if self.maker33 < 1.0:
            if self.maker48 <= 0.01:
                stops = -20.0 * self.maker48 + 1.8
            else:
                stops = -0.101 * self.maker48 + 1.601
        else:
            if self.maker48 <= 0.01:
                stops = -70.0 * self.maker48 + 3.0
            else:
                stops = -0.303 * self.maker48 + 2.303
        return 2.0 ** max(stops, 0.0)