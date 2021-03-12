/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package laboratoriofinalv2;

import java.util.ArrayList;

/**
 *
 * @author estudiante.fit
 */
public class LaboratorioFinalv2 {

    /**
     *
     *
     * @param args the command line arguments
     *
     */
    public static void main(String[] args) {

        Planta p = new Planta();
        Productor pr = new Productor(p, "productor");
        pr.start();
        Planificadores hola = new Planificadores();
        String[] datoscamiones = ManejadorArchivosGenerico.leerArchivo("C:\\Users\\estudiante.fit\\Desktop\\nerv\\camioness.txt");
        ArrayList<Vehiculo> camiones = hola.ordenarDatosTxt(datoscamiones, p);
        hola.FCFS(camiones);
        System.out.println("FIN");
        System.exit(0);

    }

}

