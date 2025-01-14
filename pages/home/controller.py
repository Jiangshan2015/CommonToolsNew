from flet_mvc import FletController


# Controller
class HomeController(FletController):
    def menu_clicked(self, e=None):
        for pg in self.model.switch_control.value:
            self.model.switch_control.value[pg].offset.x = 2
            self.model.switch_control.value[pg].update()
        self.model.switch_control.value[e].offset.x = 0
        self.model.switch_control.value[e].update()
        self.update()
