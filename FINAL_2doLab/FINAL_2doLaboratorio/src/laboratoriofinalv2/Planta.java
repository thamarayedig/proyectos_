/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package laboratoriofinalv2;

import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author estudiante.fit
 */
public class Planta {

    private int garrafas = 0;
    private boolean cargando = false;
    int contador = 0;
    int garrafasR = 0;

    public synchronized void producirGarrafas() {
        while (this.garrafas > 0 || cargando == true) {
            try {
                //System.out.println("Planta");
                wait();
            } catch (InterruptedException ex) {
                Logger.getLogger(Planta.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
        for (int i = 1; i <= 11600; i++) {
            garrafas++;

        }
        try {
            Thread.sleep(1000);
        } catch (InterruptedException ex) {
            Logger.getLogger(Planta.class.getName()).log(Level.SEVERE, null, ex);
        }
        notifyAll();

    }

    public synchronized void consumirGarrafas(int capacidad, int id, boolean lleno) {
        while (cargando == true || lleno == true || garrafas < capacidad) {
            try {
                wait();
                System.out.println("id " + id + " esperando");
            } catch (InterruptedException ex) {
                Logger.getLogger(Planta.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
        for (int i = 1; i <= capacidad; i++) {
            garrafas--;
            contador++;

            if (i == capacidad) {
                lleno = true;
                cargando = false;
                notifyAll();
                System.out.println("Se llenó el camión " + id + " con " + capacidad + " garrafas");
            }
            if (contador == 2400) {
                System.out.println("----------------------------DESCANSO DE 20 MINUTOS");
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException ex) {
                    Logger.getLogger(Planta.class.getName()).log(Level.SEVERE, null, ex);
                }
                contador = 0;
            }
        }
    }

}
