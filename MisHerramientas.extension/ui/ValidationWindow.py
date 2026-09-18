# -*- coding: utf-8 -*-

import os
import ui_models
import report
import restore

from pyrevit import forms


class ValidationWindow(forms.WPFWindow):

    def __init__(self, doc, result, report_text):
        xaml = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "ui",
            "ValidationWindow.xaml"
        )

        forms.WPFWindow.__init__(self, xaml)

        self.doc = doc
        self.result = result

        # Resumen
        self.txtNew.Text = str(len(result.New))
        self.txtDeleted.Text = str(len(result.Deleted))
        self.txtMoved.Text = str(len(result.Moved))

       
        rows = ui_models.build_rows(result)

        self.dgTopographies.ItemsSource = rows

    def btnClose_Click(self, sender, args):
        self.Close()

    def btnRestore_Click(self, sender, args):

        row = self.dgTopographies.SelectedItem

        if row is None:

            forms.alert(
                "Selecciona una topografía.",
                title="TopoGuard"
            )

            return

        if row.Change != "Movida":

            forms.alert(
                "Solo pueden restaurarse topografías movidas.",
                title="TopoGuard"
            )

            return

        respuesta = forms.alert(
            "¿Deseas restaurar '{}' a su posición registrada?".format(
                row.Name
            ),
            yes=True,
            no=True,
            title="TopoGuard"
        )

        if not respuesta:
            return

        restore.restore(
            self.doc,
            row.Data
        )

        #Mensaje de éxito
        forms.alert(
        "La topografía seleccionada ha sido restaurada exitosamente.\n\n"
        "Ha regresado a su posición original registrada.\n\n"
        "✓ Restauración completada con éxito.",
        title="TopoGuard"
)


    def dgTopographies_SelectionChanged(self, sender, args):
        row = self.dgTopographies.SelectedItem

        if row is None:
            self.txtDetails.Text = ""
            return

        self.txtDetails.Text = report.build_details(row.Data)