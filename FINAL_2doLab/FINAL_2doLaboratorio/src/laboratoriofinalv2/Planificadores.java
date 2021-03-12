/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package laboratoriofinalv2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author estudiante.fit
 */
public class Planificadores {

    public Planificadores() {
    }

    int generadorId = 1;

    public ArrayList<Vehiculo> ordenarDatosTxt(String[] datoscamiones, Planta p) {
        String[] datosseparados = new String[datoscamiones.length];
        ArrayList<Vehiculo> camiones = new ArrayList<Vehiculo>();
        for (String datoscamione : datoscamiones) {
            datosseparados = (datoscamione).split(",");
            for (int i = 0; i < datosseparados.length; i++) {
                if (i % 2 == 0) {
                    Vehiculo v = new Vehiculo(generadorId, Integer.parseInt(datosseparados[i]), p, Integer.parseInt(datosseparados[i + 1]));
                    generadorId++;
                    camiones.add(v);
                }

            }
        }
        return camiones;

    }

    public void FCFS(ArrayList<Vehiculo> camiones) {
        Collections.sort(camiones);
        System.out.println("*******************************ordenar por turno");
        for (int i = 0; i < camiones.size(); i++) {
            System.out.println("camión: " + camiones.get(i).Id + " cap: " + camiones.get(i).Capacidad + " turno: " + camiones.get(i).turno);
            camiones.get(i).start();
            try {
                camiones.get(i).join();
            } catch (InterruptedException ex) {
                Logger.getLogger(Planificadores.class.getName()).log(Level.SEVERE, null, ex);
            }
        }

        int[] tiempoCompletado = new int[camiones.size()];
        int[] tiempoEspera = new int[camiones.size()];
        int sumarC = 0;
        double historicoEspera = 0;

        for (int i = 0; i < camiones.size(); i++) {
            sumarC += camiones.get(i).Capacidad;
            tiempoCompletado[i] = +sumarC;
            tiempoEspera[i] = tiempoCompletado[i] - camiones.get(i).Capacidad;
            historicoEspera += tiempoEspera[i];
        }

        System.out.println("Camion   TiempoLlegada   Capacidad   Retorno   Espera");
        for (int i = 0; i < camiones.size(); i++) {
            System.out.println(camiones.get(i).Id + "          " + camiones.get(i).turno + "          " + camiones.get(i).Capacidad + "             " + tiempoCompletado[i] + "        " + tiempoEspera[i]);
        }
        System.out.println("----------> Espera promedio FCFS: " + (historicoEspera / camiones.size()) + " garrafas");
        System.out.println("  son " + (historicoEspera / camiones.size() / 20) + " minutos");
    }
}
