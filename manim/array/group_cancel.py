from manimlib.imports import *

class Cancel(VGroup):
    CONFIG = {
        "line_kwargs": {"color": RED},
        "buff_text": None,
        "buff_line": 0.7,
    }

    def __init__(self, text, texmob=None, **kwargs):
        digest_config(self, kwargs)
        VGroup.__init__(self, **kwargs)
        
        # read kwargs
        scale = kwargs.get('scale', 2)
        text_scale = kwargs.get('text_scale', 1)
        stroke_width = kwargs.get('stroke_width', 3)
        tip_length = kwargs.get('tip_length', .2)

        pre_coord_dl = text.get_corner(DL)
        pre_coord_ur = text.get_corner(UR)
        
        reference_line = Line(pre_coord_dl, pre_coord_ur)
        reference_line.scale(scale)

        coord_dl = reference_line.get_corner(DL)
        coord_ur = reference_line.get_corner(UR)

        #reference_unit_vector = reference_line.get_unit_vector()
        #coord_dl = text.get_corner(DL) - text.get_center() - reference_unit_vector*self.buff_line
        #coord_ur = text.get_corner(UR) - text.get_center() + reference_unit_vector*self.buff_line
        
        if texmob == None:
            line = Line(coord_dl, coord_ur, **self.line_kwargs)
            self.add(line)
        else:
            arrow = Arrow(coord_dl, coord_ur, 
                        **self.line_kwargs, 
                          stroke_width=stroke_width,
                          tip_length=tip_length)
            unit_vector = arrow.get_unit_vector()
            if self.buff_text == None:
                self.buff_text = get_norm(
                    (texmob.get_center()-texmob.get_critical_point(unit_vector))/2)*2
            texmob.move_to(arrow.get_end()+unit_vector*self.buff_text)
            texmob.scale(text_scale)
            self.add(arrow, texmob)


class CancelGroup(Scene):
    def construct(self):
        formula = TexMobject('\\lim_{x \\to \\infty}',
                             '{1 \\over',
                             'x}')

        fraction = VGroup(formula[1], formula[2])
        
        # denominator tends to infinity.
        cancel = CancelV2(formula[2], 
                        texmob=TexMobject('\\infty'), 
                        scale=3, 
                        text_scale=0.5)

        self.play(Write(formula))
        self.wait()
        self.play(ShowCreation(cancel))
        self.wait()
        
        self.remove(cancel)
        # cancel the whole fraction, tends to zero
        cancel = CancelV2(fraction, texmob=TexMobject('0'))
        self.play(ShowCreation(cancel))
        
