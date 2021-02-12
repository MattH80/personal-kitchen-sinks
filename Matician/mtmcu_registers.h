/* Corresponds to MTMCU 1.0. Refer to the MTMCU Reference Manual for details. */

#ifndef MTMCU_REGISTERS_H
#define MTMCU_REGISTERS_H

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

/* GPIO registers definition. */
typedef struct {
    volatile uint32_t ISRA;
    volatile uint32_t PCF;
    volatile uint32_t DIR;
    volatile uint32_t IDR;
    volatile uint32_t ODR;
    volatile uint32_t PU;
    volatile uint32_t PCIC;
    volatile uint32_t DF;
} GPIO_Registers;

/* TIMER registers definition. */
typedef struct {
    volatile uint32_t ISRA;
    volatile uint32_t STAT;
    volatile uint32_t CTRL;
    volatile uint32_t PSC;
    volatile uint32_t CPR;
    volatile uint32_t VAL;
} TIMER_Registers;

/* TIMER bits definition. */
#define TIMER_STAT_CPM      (1 << 1)
#define TIMER_STAT_OVF      (1 << 0)

#define TIMER_CTRL_TMEN     (1 << 8)
#define TIMER_CTRL_CPMIE    (1 << 1)
#define TIMER_CTRL_OVFIE    (1 << 0)

/* Peripheral map definition. */
#define GPIO    ((GPIO_Registers  *)0x30000000)
#define TIMER   ((TIMER_Registers *)0x30000100)

/* Disables interrupts globally. */
static inline void __disable_interrupts() {
    asm volatile("setdi");
}

/* Enables interrupts globally. */
static inline void __enable_interrupts() {
    asm volatile("clrdi");
}

/*
 * Enters the low power mode. Execution stalls until
 * an interrupt request is received.
 */
static inline void __wait_for_interrupt() {
    asm volatile("wfi");
}

#ifdef __cplusplus
}
#endif

#endif /* MTMCU_REGISTERS_H */
