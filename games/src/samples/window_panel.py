from ursina import *

'''
WindowPanel is an easy way to create UI. It will automatically layout the content.
'''
app = Ursina()
wp = WindowPanel(
    title='Custom Window',
    content=(
        Text('Name:'),
        InputField(name='name_field'),
        Button(text='Submit', color=color.azure),
        Slider(),
        Slider(),
        ButtonGroup(('test', 'eslk', 'skffk'))
        ),
    )

wp.y = wp.panel.scale_y / 2 * wp.scale_y    # center the window panel

app.run()
