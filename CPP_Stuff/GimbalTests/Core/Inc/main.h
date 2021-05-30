/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.h
  * @brief          : Header for main.c file.
  *                   This file contains the common defines of the application.
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; Copyright (c) 2021 STMicroelectronics.
  * All rights reserved.</center></h2>
  *
  * This software component is licensed by ST under BSD 3-Clause license,
  * the "License"; You may not use this file except in compliance with the
  * License. You may obtain a copy of the License at:
  *                        opensource.org/licenses/BSD-3-Clause
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __MAIN_H
#define __MAIN_H

#ifdef __cplusplus
extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
#include "stm32f4xx_hal.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Exported types ------------------------------------------------------------*/
/* USER CODE BEGIN ET */

/* USER CODE END ET */

/* Exported constants --------------------------------------------------------*/
/* USER CODE BEGIN EC */

/* USER CODE END EC */

/* Exported macro ------------------------------------------------------------*/
/* USER CODE BEGIN EM */

/* USER CODE END EM */

/* Exported functions prototypes ---------------------------------------------*/
void Error_Handler(void);

/* USER CODE BEGIN EFP */

/* USER CODE END EFP */

/* Private defines -----------------------------------------------------------*/
#define RAIL_5V_Pin GPIO_PIN_1
#define RAIL_5V_GPIO_Port GPIOC
#define LED_G_Pin GPIO_PIN_0
#define LED_G_GPIO_Port GPIOA
#define LED_B_Pin GPIO_PIN_1
#define LED_B_GPIO_Port GPIOA
#define LED_R_Pin GPIO_PIN_2
#define LED_R_GPIO_Port GPIOA
#define BUTTON_1_Pin GPIO_PIN_3
#define BUTTON_1_GPIO_Port GPIOA
#define SCK_Pin GPIO_PIN_5
#define SCK_GPIO_Port GPIOA
#define MISO_Pin GPIO_PIN_6
#define MISO_GPIO_Port GPIOA
#define MOSI_Pin GPIO_PIN_7
#define MOSI_GPIO_Port GPIOA
#define ENC_CS_Pin GPIO_PIN_4
#define ENC_CS_GPIO_Port GPIOC
#define CAN_RX_B_Pin GPIO_PIN_12
#define CAN_RX_B_GPIO_Port GPIOB
#define CAN_TX_B_Pin GPIO_PIN_13
#define CAN_TX_B_GPIO_Port GPIOB
#define LED_1_Pin GPIO_PIN_7
#define LED_1_GPIO_Port GPIOC
#define CAN_RX_A_Pin GPIO_PIN_11
#define CAN_RX_A_GPIO_Port GPIOA
#define CAN_TX_A_Pin GPIO_PIN_12
#define CAN_TX_A_GPIO_Port GPIOA
#define SWD_IO_Pin GPIO_PIN_13
#define SWD_IO_GPIO_Port GPIOA
#define SWD_CLK_Pin GPIO_PIN_14
#define SWD_CLK_GPIO_Port GPIOA
#define JTDI_Pin GPIO_PIN_15
#define JTDI_GPIO_Port GPIOA
#define UART_TX_Pin GPIO_PIN_10
#define UART_TX_GPIO_Port GPIOC
#define UART_RX_Pin GPIO_PIN_11
#define UART_RX_GPIO_Port GPIOC
#define JTDO_Pin GPIO_PIN_3
#define JTDO_GPIO_Port GPIOB
#define PITCH_SERVO_Pin GPIO_PIN_4
#define PITCH_SERVO_GPIO_Port GPIOB
#define ROLL_SERVO_Pin GPIO_PIN_5
#define ROLL_SERVO_GPIO_Port GPIOB
#define YAW_SERVO_Pin GPIO_PIN_6
#define YAW_SERVO_GPIO_Port GPIOB
/* USER CODE BEGIN Private defines */

/* USER CODE END Private defines */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
