/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package laboratoriofinalv2;

/**
 *
 * @author estudiante.fit
 */
public class Vehiculo extends Thread implements Comparable<Vehiculo> {
    
    int Id;
    int Capacidad;
    boolean lleno = false;
    Planta planta;
    int turno;
    

    public Vehiculo(int Id, int Capacidad, Planta planta, int turno) {
        this.Id = Id;
        this.Capacidad = Capacidad;
        this.planta = planta;
        this.turno = turno;
    }  
    
        @Override
    public void run(){
        planta.consumirGarrafas(Capacidad, Id, lleno);
    }
    
    @Override
    public int compareTo(Vehiculo o) {
        if (turno < o.turno) {
                return -1;
            }
            if (turno > o.turno) {
                return 1;
            }
            return 0;
    }

}
