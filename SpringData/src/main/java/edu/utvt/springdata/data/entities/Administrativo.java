package edu.utvt.springdata.data.entities;

import jakarta.persistence.DiscriminatorValue;
import jakarta.persistence.Entity;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;

@EqualsAndHashCode(callSuper = true)
@Entity
@DiscriminatorValue(value = "2")
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Administrativo extends Usuario {
    private Double salario;
}
