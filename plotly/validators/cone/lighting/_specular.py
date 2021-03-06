import _plotly_utils.basevalidators


class SpecularValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='specular', parent_name='cone.lighting', **kwargs
    ):
        super(SpecularValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            max=2,
            min=0,
            role='style',
            **kwargs
        )
