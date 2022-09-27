import os
from gi.repository import Gtk
from ..info import data_dir
from ..settings import login_screen_settings
from ..common_widgets import ImageChooserButton
from ..bind_utils import *
from .common import PageContent


class LoginScreenPageContent (PageContent):
    __gtype_name__ = 'LoginScreenPageContent'

    def __init__ (self, window, **kwargs):
        super().__init__(**kwargs)

        self.window = window

        self.builder = Gtk.Builder.new_from_file(os.path.join(data_dir, 'login-screen-page.ui'))

        self.set_child(self.builder.get_object('content_box'))

        self.disable_restart_buttons_switch = self.builder.get_object('disable_restart_buttons_switch')
        self.disable_user_list_switch = self.builder.get_object('disable_user_list_switch')
        self.welcome_message_switch = self.builder.get_object('welcome_message_switch')
        self.welcome_message_entry = self.builder.get_object('welcome_message_entry')
        self.enlarge_welcome_message_switch = self.builder.get_object('enlarge_welcome_message_switch')
        self.logo_actionrow = self.builder.get_object('logo_actionrow')
        self.logo_switch = self.builder.get_object('logo_switch')

        # Add logo button
        self.logo_button = ImageChooserButton(valign='center')
        self.logo_actionrow.add_suffix(self.logo_button)
        self.logo_actionrow.set_activatable_widget(self.logo_button)

        self.bind_to_gsettings()

    def bind_to_gsettings (self):
        bind(login_screen_settings, 'disable-restart-buttons', self.disable_restart_buttons_switch, 'active')
        bind(login_screen_settings, 'disable-user-list', self.disable_user_list_switch, 'active')
        bind(login_screen_settings, 'enable-welcome-message', self.welcome_message_switch, 'active')
        bind(login_screen_settings, 'enlarge-welcome-message', self.enlarge_welcome_message_switch, 'active')
        bind(login_screen_settings, 'welcome-message', self.welcome_message_entry, 'text')
        bind(login_screen_settings, 'enable-logo', self.logo_switch, 'active')
        bind(login_screen_settings, 'logo', self.logo_button, 'filename')
